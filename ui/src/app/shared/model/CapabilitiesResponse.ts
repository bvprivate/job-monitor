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
 * Specification of the backend's capabilities
 */
export interface CapabilitiesResponse {
    authentication?: models.AuthenticationCapability;

    /**
     * Fields on QueryJobsResult returned from POST /jobs/query populated on some or all jobs. The fields are mapped to their display names, in order of importance. Extended fields and labels can be included, such as 'label.foo' or 'extensions.userId' 
     */
    displayFields?: Array<models.DisplayField>;

    /**
     * Common labels which are present on most jobs returned
     */
    commonLabels?: Array<string>;

    /**
     * Fields on ExtendedQueryFields which are queryable
     */
    queryExtensions?: Array<string>;

}
