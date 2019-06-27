import {Component, Input, OnInit, ViewContainerRef} from '@angular/core';
import {DomSanitizer, SafeUrl} from '@angular/platform-browser';

import {AuthService} from '../../../core/auth.service';
import {ResourceUtils} from "../../../shared/utils/resource-utils";
import {GcsService} from "../../../core/gcs.service";
import {MatDialog, MatSnackBar} from "@angular/material";
import {JobResourceContentsComponent} from "./resource-contents/resource-contents.component";
import {ErrorMessageFormatterPipe} from "../../../shared/pipes/error-message-formatter.pipe";
import {JsonPipe} from "@angular/common";

@Component({
  selector: 'jm-debug-icons',
  templateUrl: './debug-icons.component.html',
  styleUrls: ['./debug-icons.component.css']
})
export class JobDebugIconsComponent implements OnInit {
  @Input() displayMessage: boolean;
  @Input() operationId: string;
  @Input() operationDetails: string;
  @Input() message: string;
  @Input() stdout: string;
  @Input() stderr: string;
  @Input() directory: string;
  logFileData: Map<string, string> = new Map();

  constructor(private readonly authService: AuthService,
              private readonly gcsService: GcsService,
              private readonly snackBar: MatSnackBar,
              private readonly sanitizer:DomSanitizer,
              public resourceContentsDialog: MatDialog) {}

  ngOnInit(): void {
    try {
      const authenticated = this.authService.isAuthenticated()
      if (authenticated && this.authService.gcsReadAccess) {
        if (this.stdout) {
          this.getLogContents(this.stdout).then((value) => {
            this.logFileData[this.getFileName(this.stdout)] = value;
          }).catch(error => {
            this.handleError(error);
          });
        }
        if (this.stderr) {
          this.getLogContents(this.stderr).then((value) => {
            this.logFileData[this.getFileName(this.stderr)] = value;
          }).catch(error => {
            this.handleError(error);
          });
        }
      }
    } catch (error) {
      this.handleError(error);
    }
  }

  getResourceUrl(url: string): string {
    if (!url || !ResourceUtils.isResourceURL(url) || (this.authService.gcsReadAccess && !this.hasContents(this.getFileName(url)))) {
      return '';
    }
    return ResourceUtils.getResourceBrowserURL(url, this.authService.userEmail);
  }

  getDirectoryUrl(directory): SafeUrl {
    if (directory && ResourceUtils.isResourceURL(directory)) {
      return this.sanitizer.bypassSecurityTrustResourceUrl(ResourceUtils.getDirectoryBrowserURL(directory, this.authService.userEmail));
    }
    return '';
  }

  hasContents(fileName: string): boolean {
    return Object.keys(this.logFileData).includes(fileName) && this.logFileData[fileName] != '';
  }

  showOrLinkTo(e: MouseEvent, url: string): void {
    e.stopPropagation();
    if (this.hasContents(this.getFileName(url))) {
      this.resourceContentsDialog.open(JobResourceContentsComponent, {
        disableClose: false,
        data: {
          resourceName: this.getFileTitle(url),
          resourceContents: this.logFileData[this.getFileName(url)],
          resourceLink: this.getResourceUrl(url),
          resourceType: 'text'
        }
      });
    } else if (url) {
      window.open(this.getResourceUrl(url));
    }
  }

  showOperationDetails(contents: string): void {
    this.resourceContentsDialog.open(JobResourceContentsComponent, {
      disableClose: false,
      data: {
        resourceName: this.operationId,
        resourceContents: new JsonPipe().transform(JSON.parse(contents)),
        resourceLink: '',
        resourceType: 'json'
      }
    });
  }

  private async getLogContents(url: string): Promise<string> {
    try {
      const bucket = ResourceUtils.getResourceBucket(url);
      const object = ResourceUtils.getResourceObject(url);
      return await this.gcsService.readObject(bucket, object)
        .then(data => data);
    } catch (error) {
      this.handleError(error);
    }
  }

  private getFileName(filePath: string): string {
    if (filePath) {
      const fileParts = filePath.split('/');
      return fileParts.pop();
    }
  }

  private getFileTitle(filePath: string): string {
    if (filePath) {
      const fileParts = filePath.split('/');
      return fileParts.slice(-2).join('/');
    }

  }

  handleError(error: any) {
    this.snackBar.open(
      new ErrorMessageFormatterPipe().transform(error),
      'Dismiss');
  }
}
