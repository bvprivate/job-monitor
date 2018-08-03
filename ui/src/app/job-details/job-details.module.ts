import {CommonModule} from '@angular/common';
import {NgModule} from '@angular/core';
import {
  MatButtonModule,
  MatCardModule,
  MatDividerModule,
  MatExpansionModule,
  MatGridListModule,
  MatListModule,
  MatMenuModule,
  MatSnackBarModule,
  MatTableModule,
  MatTabsModule,
  MatTooltipModule,
} from '@angular/material';
import {ClrIconModule, ClrTooltipModule} from '@clr/angular';

import {JobDetailsComponent} from './job-details.component';
import {JobPanelsComponent} from './panels/panels.component';
import {JobResourcesComponent} from './resources/resources.component';
import {JobResourcesTableComponent} from './resources/resources-table/resources-table.component';
import {SharedModule} from '../shared/shared.module';
import {TaskDetailsComponent} from './tasks/tasks.component';
import {GcsService} from '../core/gcs.service';
import {JobFailuresTabComponent} from './failures/failures-tab/failures-tab.component';
import {JobFailuresComponent} from './failures/failures.component';


@NgModule({
  imports: [
    ClrIconModule,
    ClrTooltipModule,
    CommonModule,
    MatButtonModule,
    MatCardModule,
    MatDividerModule,
    MatExpansionModule,
    MatGridListModule,
    MatListModule,
    MatMenuModule,
    MatSnackBarModule,
    MatTableModule,
    MatTabsModule,
    MatTooltipModule,
    SharedModule,
  ],
  declarations: [
    JobDetailsComponent,
    JobPanelsComponent,
    JobResourcesComponent,
    JobResourcesTableComponent,
    TaskDetailsComponent,
    JobFailuresComponent,
    JobFailuresTabComponent,
  ],
  providers: [
    GcsService
  ],
  exports: []
})
export class JobDetailsModule {}
