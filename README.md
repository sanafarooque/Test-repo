# Morpheus API Automation

The framework provides necessary libraries to interact with Morpheus API's (for now basic has been added)

### Folder structure:

```
.
├── README.md
├── morpheus_api
│   ├── __init__.py                     # Instantiate your classes here (only if running the script as standalone without tests/pytest)
│   ├── api_endpoints                   # Define the APIs here
│   │   ├── __init__.py
│   │   ├── clouds.py
│   │   ├── clusters.py
│   │   ├── instances.py
│   │   └── provisions.py
│   ├── configuration                   # Define the API login here
│   │   └── utils.py
│   ├── dataclasses                     # Define your dataclasses (payload) here
│   │   ├── __init__.py
│   │   ├── cloud.py
│   │   ├── cluster.py
│   │   ├── instance.py
│   │   ├── layout.py
│   │   ├── network.py
│   │   ├── plan.py
│   │   ├── provision.py
│   │   └── volume.py
│   ├── exceptions.py                   # Define and add your custom exceptions
│   └── settings.py                     # Register the newly added endpoints here
├── requirements.txt
└── tests
    ├── NA_test_clouds.py
    ├── NA_test_clusters.py
    ├── pytest.ini
    └── test_instances.py
```

## Installing Dependencies

### Pre-requisite
- JFROG credentials are required to install the library and can be set in the following way

```bash
# Mac / Linux:
export JFROG_USERNAME="username"
export JFROG_PASSWORD="password"

# Windows (Powershell):
$Env:JFROG_USERNAME="username"
$Env:JFROG_PASSWORD="password"
```

### Create virtual environment
```sh
python3 -m venv venv

# Mac / Linux:
. venv/bin/activate

# Windows
venv\Scripts\activate.bat
```

### Install dependencies

```sh
# Mac / Linux:
./install_dependencies.sh

# Windows
bash ./install_dependencies.sh
```
> NOTE: The JFROG credentials are posted in the [`#hv-qa-automation`](https://hpe-internal.slack.com/archives/C072K0L1LDQ/p1742930268099619) slack channel (pinned messages). Please reach out to @tatapraveen in case you couldn't find them

# How to Run:

- Copy the `.example.env` file to `.env.dev` with relevant values
  - Create additional `.env.*` files if needed
  - You will need to create: `.env.dev`, `.env.prod`, and `.env.scint` files. The default will be `.env.dev`
- Good to use venv; `python3.12 -m venv .venv`
  - Then do: `source .venv/bin/activate`
- Run `pip install -r requirements_freeze.txt`
- From the current working directory (root of the project) execute: `pytest -svra tests/test_instances.py`
  - Based on the environment you are running on, pass relevant environment variable. For example, SCINT runs will need to follow: `ENVIRONMENT=scint pytest -svra tests/test_instances.py`

> [!IMPORTANT]
> Code was tested using `Python 3.12`

> [!WARNING]
> You might encounter the following issues:

    - If you get JSON error, then do the following:

        - `pip install --upgrade werkzeug`

    - If you get ModuleNotFound error then do the following:

        - `export PYTHONPATH=$(pwd)`

> [!WARNING]
> Morpheus Team (Tommy) responded -> that storage-volumes API's purpose is strictly for Infrastructure > Storage > Volumes with very limited scenarios (not with WS4), can't delete a disk from an instance, it needs to be reconfigured

# Sample Output:

```
(.morph) ➜  Morpheus pytest -svra tests/test_instances.py
========================================== test session starts ===========================================
platform darwin -- Python 3.12.5, pytest-8.3.3, pluggy-1.5.0 -- /Users/uplaonka/Desktop/Sachin/2024/Morpheus/.morph/bin/python
cachedir: .pytest_cache
rootdir: /Users/uplaonka/Desktop/Sachin/2024/Morpheus/tests
configfile: pytest.ini
collected 1 item

tests/test_instances.py::test_create_and_list_instance Instance created successfully: {'instance': {'id': 96, 'uuid': '927e9c25-66bf-4b1a-8062-fa888ed8bf31', 'accountId': 1, 'tenant': {'id': 1, 'name': 'pqa-setup-8'}, 'instanceType': {'id': 44, 'code': 'mvm', 'category': 'cloud', 'name': 'MVM', 'image': '/assets/branding/140x40/mvm.svg'}, 'group': {'id': 1, 'name': 'pqa-group'}, 'cloud': {'id': 1, 'name': 'qa-cloud', 'type': 'standard'}, 'cluster': {'id': 2, 'name': 'cluster8', 'type': {'id': 4, 'code': 'mvm-cluster', 'name': 'MVM Cluster (Open Beta)'}}, 'containers': [108], 'servers': [116], 'resources': [], 'connectionInfo': [{'ip': '0.0.0.0', 'port': None, 'name': None}], 'layout': {'id': 269, 'name': 'Single MVM VM', 'provisionTypeId': 5, 'provisionTypeCode': 'kvm'}, 'plan': {'id': 152, 'code': 'kvm-vm-1024', 'name': '1 CPU, 1GB Memory'}, 'name': 'python-mvm-sep19-7', 'displayName': 'python-mvm-sep19-7', 'description': None, 'environment': 'qa', 'config': {'poolProviderType': 'mvm', 'imageId': '402', 'resourcePoolId': 'pool-2', 'createUser': False, 'expose': 8080, 'kvmHostId': 4, 'noAgent': False, 'customOptions': {}, 'createBackup': True, 'memoryDisplay': 'MB', 'layoutSize': 1, 'lbInstances': None}, 'configGroup': None, 'configId': None, 'configRole': None, 'volumes': [{'id': -1, 'name': 'root', 'size': 1, 'sizeId': None, 'datastoreId': '4', 'rootVolume': True, 'storageType': None, 'maxIOPS': None, 'resizeable': None, 'controllerMountPoint': None}], 'controllers': [], 'interfaces': [{'id': None, 'row': 0, 'network': {'id': 4, 'subnet': None, 'group': None, 'dhcpServer': True, 'name': 'Management', 'pool': None}, 'ipAddress': None, 'ipMode': '', 'networkInterfaceTypeId': None}], 'customOptions': {}, 'instanceVersion': '1.0', 'labels': [], 'tags': [], 'evars': [{'name': 'MVM_IP', 'value': '0.0.0.0', 'export': True, 'masked': False}, {'name': 'MVM_HOST', 'value': 'container108', 'export': True, 'masked': False}], 'maxMemory': 1073741824, 'maxStorage': 1073741824, 'maxCores': 1, 'coresPerSocket': 1, 'maxCpu': None, 'hourlyCost': 0.0, 'hourlyPrice': 0.0, 'instancePrice': None, 'dateCreated': '2024-09-20T00:35:33Z', 'lastUpdated': '2024-09-20T00:35:34Z', 'hostName': 'python-mvm-sep19-7', 'domainName': None, 'environmentPrefix': None, 'firewallEnabled': True, 'networkLevel': 'container', 'autoScale': False, 'instanceContext': 'qa', 'currentDeployId': None, 'locked': False, 'status': 'pending', 'statusMessage': None, 'errorMessage': None, 'statusDate': None, 'statusPercent': None, 'statusEta': None, 'userStatus': None, 'expireDays': None, 'renewDays': None, 'expireCount': 0, 'expireDate': None, 'expireWarningDate': None, 'expireWarningSent': False, 'shutdownDays': None, 'shutdownRenewDays': None, 'shutdownCount': 0, 'shutdownDate': None, 'shutdownWarningDate': None, 'shutdownWarningSent': False, 'removalDate': None, 'createdBy': {'id': 14, 'username': 'sachin'}, 'owner': {'id': 14, 'username': 'sachin'}, 'notes': None, 'powerSchedule': None, 'isScalable': None, 'instanceThreshold': None, 'isBusy': None, 'apps': []}, 'success': True}
Instance 'python-mvm-sep19-7' created with ID: 96

Instance 'python-mvm-sep19-7' created and found in the list.
PASSED

=========================================== 1 passed in 5.90s ============================================
(.morph) ➜  Morpheus
```

## Instance in Morpheus Appliance

Most parameters are dynamically retrieved using service APIs.
The following values are currently hardcoded from the 'env' file:

- SITE_ID
- LAYOUT_SIZE
- CONFIG["resourcePoolId"]

![provisioned instance](./images/Screenshot%202024-09-20%20at%205.46.02 AM.png)

## PR Checks:

Each PR is checked for the following:

- Linting errors
- Formatting errors using `black` formatter
- Pytest collection

This is carried out using GitHub Actions workflow. Workflow file used for PR checks: [pr-checks.yml](https://github.com/hpe-cds/morpheus-qa-automation/blob/main/.github/workflows/pr-checks.yml)

## Deploying to GitHub pages:

With each PR, github docs are generated and deployed to [GitHub Pages](https://symmetrical-happiness-g6411e1.pages.github.io/)
The docs contain all the classes and their function definitions.
To make this process efficient, please make sure that all the functions and classes have good docstring

💡 We can use github co-pilot to generate docstring 😉

> [!NOTE] GitHub Pages config is a one time setup activity

#### Config

For the deployment to work, we need to configure the following:

- Navigate to `Settings > Pages`
- Select `Deploy from a branch` under `Source`
- Select `gh-pages` and `/root` folder under `Branch`

#### Deployment Process

- Each PR generates docs using the `pdco3` library
  - [generate_docs](https://github.com/hpe-cds/morpheus-qa-automation/actions/workflows/generate_docs.yml) job
  - [generate_docs.yml](https://github.com/hpe-cds/morpheus-qa-automation/blob/main/.github/workflows/generate_docs.yml) workflow file
- The docs are committed to the `github-pages` branch
- Once the PR is merged, a new github actions workflow is triggered which deploys the docs to GitHub pages
  - [pages-build-deployment](https://github.com/hpe-cds/morpheus-qa-automation/actions/workflows/pages/pages-build-deployment) job

## Test Pipelines:

All test pipeline are configured of DCS Jenkins

![image](https://github.com/user-attachments/assets/b16b296c-7950-477f-9a23-af5faaaeeeaf)

### Configuration:

- All tests will use Docker to run the tests: [Dockerfile](https://github.com/hpe-cds/morpheus-qa-automation/blob/main/Dockerfile)
- A [Jenkins job](http://dcs-jenkins-cxo.vlab.nimblestorage.com:8080/job/build-morpheus-qa-automation-docker-image/) builds the docker image on each `main` merge [Docker Registry](https://hub.docker.hpecorp.net/repositories?namespace=morpheus)

### Jobs

- [Sanity Tests](http://dcs-jenkins-cxo.vlab.nimblestorage.com:8080/job/morpheus-qa-automation-sanity-suite/)

### Dev Container

Test container is supported on this repo and tested on VSCode. Install the vscode devcontainer extension.

- From the command palette run `>devContainers: reopen in container`
