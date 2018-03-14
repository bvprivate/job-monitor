/**
 * Job Manager Service
 * Job Manager API for interacting with asynchronous batch jobs and workflows.
 *
 * OpenAPI spec version: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

import * as models from './models';

/**
 * Extended fields on jobs which may not be populated by all backends. See the /capabilities endpoint for more details. 
 */
export interface ExtendedFields {
    /**
     * The user associated with the job.
     */
    userId?: string;

    /**
     * Longer text description of the job status.
     */
    statusDetail?: string;

    /**
     * Map of type of log file to its file location.
     */
    logs?: any;

    /**
     * Job last update datetime in ISO8601 format.
     */
    lastUpdate?: Date;

    /**
     * Map of ENV variables key values associated with the job.
     */
    envs?: any;

    /**
     * The text of the script executed by this job.
     */
    script?: string;

    /**
     * The parent job ID for the job.
     */
    parentJobId?: string;

    /**
     * URL for tasks timing diagram.
     */
    timingUrl?: string;

    tasks?: Array<models.TaskMetadata>;

}
