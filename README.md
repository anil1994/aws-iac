
#  Multi-Stack AWS CDK Infrastructure as Code Project for Lambda and Container Projects

I prepare aws environment by using cdk for my two projects. You can see my application repositories as following,

## Application Repositories

* serverless app: https://github.com/anil1994/lambda-csv-to-dynamodb
* containerised app: https://github.com/anil1994/containerized-python-app


For cdk installation, I used free tier amazon linux ami server. My all installations as shown below step  are made on this server.


## There are three prerequirements for this cdk project as shown below.


# 1- Install nodejs (Attention: larger than 16.3.0 version has not tested on the cdk yet)

* https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.html
 You can change node version by running below command. For example, If you want to switch node version as 16.3.0,

```
$ nvm install 16.3.0
```
```
To download cdk v1, you can use below command.

$ npm install  aws-cdk@1.106.0
```
If you want to use cdk v2, you shoud use npm install -g aws-cdk to download latest version.

# 2- Install aws cli
You can install by following this documentation according to your operating system.
* https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
After aws cli installation, you can run command as shown below in order to adjust our aws account.

```
$ aws configure
```

# 3- Install python >= 3.6

I used cdk v1 for this cdk project. If you want, you can use cdk v2. V2 is GA now. But two versions are  different from each other. You consider syntax changes and  version incompatible issue (between cdk and python) between two versions cdkv1 and cdkv2.     

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`lambda`) and ('container')

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt

For the cdk v1, setup.py is generated automaticly, after you run command as shown below.

$ cdk init app --language python // this command generates cdk templates
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source codes, contained in the lambda and container directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
