import {Component, Inject} from "@angular/core";
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material";
import {DisplayField} from "../../../shared/model/DisplayField";

@Component({
  selector: 'jm-bulk-edit-component',
  templateUrl: 'bulk-edit.component.html',
  styleUrls: ['bulk-edit.component.css']
})
export class JobsBulkEditComponent {
  constructor(
    public dialogRef: MatDialogRef<JobsBulkEditComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any) { }

  cancelChanges(): void {
    this.dialogRef.close();
  }

  getFieldType(df: DisplayField): string {
    return df.fieldType.toString();
  }

  getFieldOptions(df: DisplayField): string[] {
    return df.validFieldValues;
  }

  getFieldDefaultValue(displayFieldItem: {
    default: string|null,
    displayField: DisplayField }): string {
    if (displayFieldItem.default !== null) {
      return displayFieldItem.default
    } else {
      return '(multiple)';
    }
  }

  setFieldValue(df: DisplayField, value: string): void {
    this.data.newValues[df.field] = value;
  }

  clearFieldValue(labelField: DisplayField, bulkEditFieldInput: HTMLInputElement): void {
    bulkEditFieldInput.value = '';
    this.setFieldValue(labelField, '');
  }

  saveChanges() {
    this.dialogRef.close({
      'fields': this.data.newValues,
      'jobs': this.data.selectedJobs
    });
  }
}