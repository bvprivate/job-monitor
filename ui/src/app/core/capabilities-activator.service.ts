import {ActivatedRouteSnapshot, RouterStateSnapshot, Router} from '@angular/router';
import {CanActivate} from '@angular/router';
import {Injectable} from '@angular/core';

import {AuthService} from './auth.service';
import {CapabilitiesResponse} from '../shared/model/CapabilitiesResponse';
import {CapabilitiesService} from './capabilities.service';
import {environment} from '../../environments/environment';
import {URLSearchParamsUtils} from '../shared/utils/url-search-params.utils'

/** Service wrapper for routing based on current authentication state. */
@Injectable()
export class CapabilitiesActivator implements CanActivate {

  constructor(
    private readonly authService: AuthService,
    private readonly capabilitiesService: CapabilitiesService,
    private readonly router: Router) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Promise<boolean> {
    return this.capabilitiesService.getCapabilities()
      .then(cap => this.handleAuthCapabilities(cap, route.routeConfig.path, state.url))
      .then(cap => this.handleProjectCapabilities(cap, route))
      .catch(reason => {
          // Handle all not-activated errors by just returning false for
          // this promise. All others, re-throw them.
          if (reason == 'not-activated') {
            return false;
          }
          throw reason;
        });
  }

  private handleAuthCapabilities(capabilities: CapabilitiesResponse, path: String, url: String): Promise<CapabilitiesResponse> {
    if (capabilities.authentication && capabilities.authentication.isRequired) {
      if (this.authService.authenticated.getValue() || path == 'sign_in') {
        return Promise.resolve(capabilities);
      }

      return this.authService.isAuthenticated().then( (authenticated) => {
        if (!authenticated) {
          this.router.navigate(['sign_in'], {
            queryParams: { returnUrl: url }
          });
          return Promise.reject('not-activated')
        }
        return Promise.resolve(capabilities);
      })
    } else if (path == 'sign_in') {
      // Do not allow navigation to the sign in page when authentication is
      // not required.
      this.router.navigate(['']);
      return Promise.reject('not-activated')
    }
  }

  private handleProjectCapabilities(capabilities: CapabilitiesResponse, route: ActivatedRouteSnapshot): Promise<boolean> {
    // Use presence of `projectId` queryExtension as an indicator that a
    // project must be selected.
    if (capabilities.queryExtensions.includes('projectId')) {
      // If we do not already have a project specified in the URL query
      // params, navigate to the projects page.
      let queryRequest = URLSearchParamsUtils.unpackURLSearchParams(route.queryParams['q']);
      if (!queryRequest.extensions.projectId && !['projects', 'sign_in'].includes(route.routeConfig.path)) {
        this.router.navigate(['projects']);
        return Promise.reject('not-activated')
      }
    } else if (route.routeConfig.path == 'projects') {
      // Do not allow navigation to the projects page when projectId is not
      // specified as a query extension.
      this.router.navigate(['']);
      return Promise.reject('not-activated')
    }
    return Promise.resolve(true);
  }
}
