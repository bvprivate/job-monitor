# Quickstart for Terra Devs

This document is intended for folks who need to do basic JobManager maintenance
in support of its use in Terra. 

## Running JobManager Locally

These are the minimal steps you need to take to get JobManager running locally in 
Docker, showing state from a local Cromwell instance. It combines steps from the 
main README and Cromwell server README.

### Check out and configure JobManager

```
$ git clone https://github.com/DataBiosphere/job-manager.git
$ cd job-manager
$ ln -sf cromwell-instance-compose.yml docker-compose.yml
```

### Set CROMWELL_URL env var

JobManager relies on a `CROMWELL_URL` environment variable to find Cromwell.
Set this to `http://IP_ADDR:8000/api/workflows/v1` where `IP_ADDR` is your machine's 
IP address. We need the broadcast address, because if we use `0.0.0.0` or `localhost` Docker
will try to connect to itself.

For example:
```
$ ifconfig | grep inet | grep broadcast
    inet 192.XXX.Y.ZZZ netmask 0xffffff00 broadcast 192.XXX.Y.255
$ export CROMWELL_URL="http://192.XXX.Y.ZZZ:8000/api/workflows/v1"
```
or the one-liner:
```
$ export CROMWELL_URL="http://$(ifconfig | grep inet | grep broadcast | cut -d ' ' -f 2):8000/api/workflows/v1"
```

### Start JobManager

```
$ docker-compose up
```
Once you see `webpack: Compiled successfully.` you should be able to access JobManager
at http://localhost:4200, and state of your local Cromwell should be reflected there.

To also rebuild the docker images:
```
$ docker-compose --build
```
Building the Job Manager UI docker image will invoke `yarn install` to generate a fresh
`node_modules` from `yarn.lock` (see `ui/Dockerfile.dev`). This may seem redundant if you have a
`node_modules` from running `yarn install` yourself. However, it better mimics what happens in
`ui/Dockerfile` for production builds and is therefore a better check that production builds will
work the same as local testing.

## Releasing JobManager in Terra

Start by following release instructions in [the README](README.md#build-docker-images-and-releases).
Once the new version exists in GCR and Github:
 * Update version in [dsp-jenkins](https://github.com/broadinstitute/dsp-jenkins/blob/master/src/main/resources/FirecloudAutomatedTesting.conf)
 * Update version in [terra-helmfile](https://github.com/broadinstitute/terra-helmfile/blob/master/versions/app/dev.yaml)