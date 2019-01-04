import {BehaviorSubject} from 'rxjs/BehaviorSubject';
import {
  Component,
  Input,
  OnChanges,
  OnInit,
  SimpleChanges
} from '@angular/core';
import {DataSource} from '@angular/cdk/collections';
import {Observable} from 'rxjs/Observable';

import {JobMetadataResponse} from '../../shared/model/JobMetadataResponse';
import {JobStatus} from '../../shared/model/JobStatus';
import {JobStatusIcon} from '../../shared/common';
import {ResourceUtils} from '../../shared/utils/resource-utils';
import {TaskMetadata} from '../../shared/model/TaskMetadata';

@Component({
  selector: 'jm-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css'],
})
export class TaskDetailsComponent implements OnInit, OnChanges {
  @Input() tasks: TaskMetadata[] = [];
  @Input() job: JobMetadataResponse;
  @Input() selectedTab: number;

  database = new TasksDatabase(this.tasks);
  dataSource: TasksDataSource | null;
  displayedColumns = [
    'name',
    'status',
    'startTime',
    'duration',
    'attempts',
    'files',
  ];

  ngOnInit() {
    this.dataSource = new TasksDataSource(this.database);
    if (this.hasCallCachedTask() || this.hasScatteredTask()) {
      this.displayedColumns.splice(1, 0, "taskInfoIcons");
    }
  }

  ngOnChanges(changes: SimpleChanges) {
    this.tasks = changes.tasks.currentValue;
    this.database.dataChange.next(this.tasks);
  }

  getStatusIcon(status: JobStatus): string {
    return JobStatusIcon[status];
  }

  getResourceUrl(url: string): string {
    return ResourceUtils.getResourceURL(url);
  }

  getTaskDirectory(task: TaskMetadata): string {
    if (task.callRoot) {
      return ResourceUtils.getDirectoryBrowserURL(task.callRoot);
    }
  }

  hasTimingUrl(): boolean {
    return this.job.extensions && !!this.job.extensions.timingUrl;
  }

  hasCallCachedTask(): boolean {
    if (this.tasks.find(t => t.callCached === true)) {
      return true;
    }
    return false;
  }

  hasScatteredTask(): boolean {
    if (this.tasks.find(t => t.shardStatuses !== null)) {
      return true;
    }
    return false;
  }

  hasFailures(): boolean {
    return this.job.failures && (this.job.failures.length > 1)
  }

  hasInputs(): boolean {
    return this.job.inputs && (Object.keys(this.job.inputs).length > 1)
  }

  hasOutputs(): boolean {
    return this.job.outputs && (Object.keys(this.job.outputs).length > 1)
  }

  getScatteredCountTotal(task: TaskMetadata): number {
    if (task.shardStatuses) {
      let count = 0;
      task.shardStatuses.forEach((status) => {
        count += status.count;
      });
      return count;
    }
  }

  // these are the shard statuses we care about
  getShardStatuses(): JobStatus[] {
    return [JobStatus.Succeeded,
            JobStatus.Failed,
            JobStatus.Running,
            JobStatus.Submitted];
   }

  getShardCountByStatus(task:TaskMetadata, status:JobStatus): number {
    let result = 0
    if(task.shardStatuses) {
      task.shardStatuses.forEach((thisStatus) => {
        if (status == thisStatus.status) {
          result = thisStatus.count;
          return;
        }
      });
    }
    return result;
  }
}

/** Simple database with an observable list of jobs to be subscribed to by the
 *  DataSource. */
export class TasksDatabase {
  private tasks: TaskMetadata[];
  /** Stream that emits whenever the data has been modified. */
  dataChange: BehaviorSubject<TaskMetadata[]> =
    new BehaviorSubject<TaskMetadata[]>(this.tasks);
  get data(): TaskMetadata[] { return this.dataChange.value; }

  constructor(tasks: TaskMetadata[]) {
    this.tasks = tasks;
    this.dataChange.next(this.tasks);
  }
}

/** DataSource providing the list of tasks to be rendered in the table. */
export class TasksDataSource extends DataSource<any> {
  tasks: TaskMetadata[];

  constructor(private _db: TasksDatabase) {
    super();
  }

  connect(): Observable<TaskMetadata[]> {
    const displayDataChanges = [
      this._db.dataChange,
    ];

    return Observable.merge(...displayDataChanges).map(() => {
      if (this._db.data) {
        return this._db.data.slice();
      }
    });
  }

  disconnect() {}
}
