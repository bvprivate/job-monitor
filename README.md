# Job Manager

[![CircleCI](https://circleci.com/gh/DataBiosphere/job-manager/tree/master.svg?style=svg)](https://circleci.com/gh/DataBiosphere/job-manager/tree/master)

_This product is in Alpha and not yet ready for production use. We welcome all feedback!_

See the [development guide](#development) below.

The Job Manager is an API and UI for monitoring and managing jobs in a backend execution engine.

The Broad, Verily, and many other organizations in the life sciences execute enormous numbers of scientific workflows and need to manage those operations. Job Manager was born out of the experiences of producing data for some of the world’s largest sequencing projects such as The Cancer Genome Atlas, Baseline, and the Thousand Genomes Project.

The Job Manager aspires to bring ease and efficiency to developing and debugging workflows while seamlessly scaling to production operations management.

## Key Features
* Supports visualization over [Cromwell](https://github.com/broadinstitute/cromwell) or [dsub](https://github.com/googlegenomics/dsub) backends
* Service provider interface can be extended to support other engines
* Rich search capabilities across current and historic workflows
* Aborting workflows
* Clean, intuitive UX based on material design principles

### Future Features
* Dynamic grouping, filtering, and drill-down
* Re-launching workflows
* Simplified troubleshooting of failed workflows
* Improved UI design

## Roadmap

The current code is a work in progress towards an alpha release and as such has started with core features: connecting to both backends, visualizing workflow and task status and metadata, quick access to log files, and simple filtering.

The near-term roadmap includes improvements to failure troubleshooting, creating a robust dashboard for grouping jobs and seeing status overviews, and improving handling of widely scattered workflows.

We envision a product with user-customizable views of jobs running, insights into workflow compute cost, the ability to re-launch jobs, and the potential to make custom reports about the jobs that have been run.

## Architecture Overview

The Job Manager [defines an API](api/jobs.yaml) via OpenAPI. An Angular2 UI is provided over the autogenerated Typescript bindings for this API. The UI is configurable at compilation time to support various deployment environments (see [environment.ts](ui/src/environments/environment.ts)), including auth, cloud projects, and label columns.

The UI must be deployed along with a backend implementation of the API, two such implementations are provided here:

### Cromwell
Monitors jobs launched by the [Cromwell workflow engine](https://github.com/broadinstitute/cromwell). The Python Flask wrapper was created using Swagger Codegen and can be configured to pull data from a specific Cromwell instance. _At this time, to utilize all job manager features, please consider using Cromwell v32 or newer._

### dsub

Monitors jobs that were launched via the [dsub](https://github.com/googlegenomics/dsub) CLI. Thin stateless wrapper around the dsub Python library. Authorization is required for deploying the UI, which is used to communicate with the [Google Genomics Pipelines API](https://cloud.google.com/genomics/pipelines). The wrapper itself is implemented in Python Flask using Swagger codegen models. A Dockerfile is provided which serves for production deployment using gunicorn.

Note that a “task” in dsub nomenclature corresponds to a Job Manager API’s “job”.

## Development

### Prerequisites

- Install docker and docker-compose
- Check out the repository and navigate to the directory:
  ```sh
    git clone https://github.com/DataBiosphere/job-manager.git
    cd job-manager
  ```
- Setup git-secrets on the repository:
  - On Mac:
  ```
  brew install git-secrets
  ```

  - On Linux:
  ```
  rm -rf git-secrets
  git clone https://github.com/awslabs/git-secrets.git
  cd git-secrets
  sudo make install && sudo chmod o+rx /usr/local/bin/git-secrets
  cd ..
  rm -rf git-secrets
  ```

- Configure the `git secrets` hook:
  ```sh
    git secrets --install
  ```

### Server Setup

- Choose your own adventure: `cromwell` (local or CaaS) or `dsub`!


#### Cromwell

- Link your preferred backend docker compose file as `docker-compose.yml`:

  - Cromwell (local): `ln -sf cromwell-local-compose.yml docker-compose.yml`
  - Cromwell (CaaS): `ln -sf cromwell-caas-compose.yml docker-compose.yml`
- Follow [servers/cromwell](servers/cromwell/README.md#Development) for Cromwell server setup then return here to continue.

#### dsub

- Link the dsub docker compose file as `docker-compose.yml`:
```sh
ln -sf dsub-local-compose.yml docker-compose.yml
```
  - If you prefer not to create a symbolic link, use:
```sh
docker-compose -f dsub-google-compose.yml CMD
```
- Set up the server for development with [`dsub`](https://github.com/googlegenomics/dsub): details in [servers/dsub](servers/dsub/README.md#Development).


### Run Locally
- Run `docker-compose up` from the root of the repository:
  - If this is the first time running `docker-compose up`  this might take a few minutes.
  - Eventually you should see a compilation success message like this: 
  ```
  jmui_1        | webpack: Compiled successfully.
  ```
- Make sure that your backend (eg the Cromwell service or dsub) is ready to receive query requests. 
- Navigate to http://localhost:4200.

#### Notes
1. Websocket reload on code change does not work in docker-compose (see
https://github.com/angular/angular-cli/issues/6349).
2. Changes to `package.json` or `requirements.txt` or [regenerating the API](#updating-the-api-using-swagger-codegen) require a rebuild with:
  ```
  docker-compose up --build
  ```
  Alternatively, rebuild a single component:
  ```
  docker-compose build ui
  ```

### Updating the API using swagger-codegen

We use [swagger-codegen](https://github.com/swagger-api/swagger-codegen) to automatically implement the API, as defined in `api/jobs.yaml`, for all
servers and the UI. Whenever the API is updated, follow these steps to update the server implementations:

#### Scripted

From the base of the checked-out job-manager repository, run:
```sh
scripts/rebuild_swagger.sh
```

#### Manually

If you prefer to perform the steps manually, you can:

1. If you do not already have the jar, you can download it here:
    ```
    # Linux
    wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.2.3/swagger-codegen-cli-2.2.3.jar -O swagger-codegen-cli.jar
    # macOS
    brew install swagger-codegen
    ```
2. Clear out existing generated models:
    ```
    rm ui/src/app/shared/model/*
    rm servers/dsub/jobs/models/*
    rm servers/cromwell/jobs/models/*
    ```
3. Regenerate both the python and angular definitions.
    ```
    java -jar swagger-codegen-cli.jar generate \
      -i api/jobs.yaml \
      -l typescript-angular2 \
      -o ui/src/app/shared
      java -jar swagger-codegen-cli.jar generate \
      -i api/jobs.yaml \
      -l python-flask \
      -o servers/dsub \
      -DsupportPython2=true,packageName=jobs
      java -jar swagger-codegen-cli.jar generate \
      -i api/jobs.yaml \
      -l python-flask \
      -o servers/cromwell \
      -DsupportPython2=true,packageName=jobs
      ```
4. Update the server implementations to resolve any broken dependencies on old API definitions or implement additional functionality to match the new specs.

## Job Manager UI Server
For UI server documentation, see [ui](ui/).

## Job Manager `dsub` Server
For `dsub` server documentation, see [servers/dsub](servers/dsub/README.md).

## Job Manager `cromwell` Server
For `cromwell` server documentation, see [servers/cromwell](servers/cromwell/README.md).

## Build docker images and releases

### How to build

From v0.2.0, Job Manager starts to release stock docker images on [DockerHub](https://hub.docker.com/u/databiosphere)

- To build the `job-manager-ui` image with `$TAG` from the root of this Github repository:
    ```
    cd ui && docker build -t job-manager-ui:$TAG . -f Dockerfile
    ```
    
- **Cromwell:** To build the `job-manager-api-cromwell` image with `$TAG` from the root of this Github repository:
    ```
    docker build -t job-manager-api-cromwell:v0.2.0 . -f servers/cromwell/Dockerfile
    ```
    
- **dsub:** To build the `job-manager-api-dsub` image with `$TAG` from the root of this Github repository:
    ```
    cd servers && docker build -t job-manager-api-dsub:v0.2.0 . -f dsub/Dockerfile
    ```

### Add a github release pointing to the dockerhub images

From v0.2.0, each release in Github will also release 3 corresponding docker images on Docker Hub:

- [job-manager-ui](https://hub.docker.com/r/databiosphere/job-manager-ui/)
- [job-manager-api-cromwell](https://hub.docker.com/r/databiosphere/job-manager-api-cromwell/)
- [job-manager-api-dsub](https://hub.docker.com/r/databiosphere/job-manager-api-dsub/)

For a long-term plan, we will set up a docker build hook so the release process can be more automated.
