import {Headers, Http, RequestOptions, Response} from '@angular/http';
import {Injectable} from '@angular/core';
import 'rxjs/add/operator/toPromise';

import {AuthService} from './auth.service';
import {environment} from '../../environments/environment';
import {QueryJobsRequest} from '../shared/model/QueryJobsRequest';
import {QueryJobsResponse} from '../shared/model/QueryJobsResponse';
import {JobMetadataResponse} from '../shared/model/JobMetadataResponse';
import {UpdateJobLabelsRequest} from "../shared/model/UpdateJobLabelsRequest";
import {UpdateJobLabelsResponse} from "../shared/model/UpdateJobLabelsResponse";


/** Service wrapper for accessing the job manager API. */
@Injectable()
export class JobManagerService {

  private static readonly defaultErrorDetail = "An unknown error has ocurred. Please try again later.";
  private static readonly defaultErrorTitle = "Unknown";

  constructor(private readonly authService: AuthService, private http: Http) {}

  private convertToJobMetadataResponse(json: object): JobMetadataResponse {
    var metadata: JobMetadataResponse = json as JobMetadataResponse;
    metadata.submission = new Date(metadata.submission);
    if (metadata.start) {
      metadata.start = new Date(metadata.start);
    }
    if (metadata.end) {
      metadata.end = new Date(metadata.end);
    }
    if (metadata.extensions) {
      if (metadata.extensions.tasks) {
        metadata.extensions.tasks.forEach((t) => {
          if (t.start) {
            t.start = new Date(t.start);
          }
          if (t.end) {
            t.end = new Date(t.end);
          }
          return t;
        });
      }
    }
    return metadata;
  }

  private convertToQueryJobsResponse(json: object): QueryJobsResponse {
    var response: QueryJobsResponse = json as QueryJobsResponse;
    for (var result of response.results) {
      result.submission = new Date(result.submission);
      if (result.start) {
        result.start = new Date(result.start);
      }
      if (result.end) {
        result.end = new Date(result.end);
      }
    }
    return response;
  }

  private respToJson(response: Response) {
    try {
      return response.json();
    } catch (_) {
      return {};
    }
  }

  private getErrorTitle(response: Response): string {
    const json = this.respToJson(response);
    if (json["title"]) {
      return json["title"];
    }
    return response.statusText ? response.statusText : JobManagerService.defaultErrorTitle;
  }

  private getErrorDetail(response: Response): string {
    const json = this.respToJson(response);
    return json["detail"] ? json["detail"] : JobManagerService.defaultErrorDetail;
  }

  private getHttpHeaders(): Headers {
    var headers = new Headers({'Content-Type': 'application/json'});
    if (this.authService.authToken) {
      headers.set('Authentication', `Bearer ${this.authService.authToken}`);
    }
    return headers;
  }

  private handleError(response: Response): Promise<any> {
    return Promise.reject({
      status: response["status"],
      title: this.getErrorTitle(response),
      message: this.getErrorDetail(response),
    });
  }

  abortJob(id: string): Promise<void> {
    return this.http.post(`${environment.apiUrl}/jobs/${id}/abort`,
      {},
      new RequestOptions({headers: this.getHttpHeaders()}))
      .toPromise()
      .then(response => response.status == 200)
      .catch((e) => this.handleError(e));
  }

  updateJobLabels(id: string, req: UpdateJobLabelsRequest): Promise<void> {
    return this.http.post(`${environment.apiUrl}/jobs/${id}/updateLabels`,
      req,
      new RequestOptions({headers: this.getHttpHeaders()}))
      .toPromise()
      .then((response) => response.status == 200)
      .catch((e) => this.handleError(e));
  }

  getJob(id: string): Promise<JobMetadataResponse> {
    return this.http.get(`${environment.apiUrl}/jobs/${id}`,
      new RequestOptions({headers: this.getHttpHeaders()}))
      .toPromise()
      .then(response => this.convertToJobMetadataResponse(response.json()))
      .catch((e) => this.handleError(e));
  }

  // TODO(calbach): Evaluate whether this should use an Observable instead for
  // consistency with other ng2 APIs, in addition to the retry/cancel
  // capabilities.
  queryJobs(req: QueryJobsRequest): Promise<QueryJobsResponse> {
    return this.http.post(`${environment.apiUrl}/jobs/query`,
      req,
      new RequestOptions({headers: this.getHttpHeaders()}))
      .toPromise()
      .then(response => this.convertToQueryJobsResponse(response.json()))
      .catch((e) => this.handleError(e));
  }
}
