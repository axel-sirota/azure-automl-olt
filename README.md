# Welcome to Automated Machine Learning with Microsoft Azure!

If you have any questions please contact me at:
Mail: axel.sirota@gmail.com
Twitter: @AxelSirota
Linkedin: Axel Sirota


## Setup

To make the best use of class time, complete the following instructions ahead of class.

**IMPORTANT NOTE: There will be some Azure fees incurred if you choose to go through the course exercises. Please read the instructions very carefully.**

1. Clone the course GitHub repo locally

    - Clone https://github.com/axel-sirota/azure-automl-olt to your local machine.

2. Create an Azure account

    - Go to https://azure.microsoft.com/en-us/free/search/ and click **Start free** .
    - You will need to login to your microsoft account (or create one)
    - You’ll need to provide a credit card to sign up.
    - Select the Free Subscription.
    - Go to https://portal.azure.com and login.
    
3. Create an ML workspace

    - On the top Search Bar type: `Machine Learning` and click the resource saying **Machine Learning** with an erlenmeyer icon
    - Click on **Create Machine Learning workspace** 
    - Under Resource Group click **create new** and type a name. For example, `auto-ml-olt`.
    - On workspace name type something unique. For example, `auto-ml-olt-0001` (use random digits)
    - Click **Review and Create** and further on, click **Create**

Now click on Go to Resource and later on, Launch Studio.

4. Create the Compute instance for the notebooks.

    - On the left panel of the Studio, click on **Compute > New**
    - Go with the recommended options and click **Next**
    - Type a name, for example, `auto-ml-instance001` (use random digits for it to be unique)
    - Click on **Create**, and wait for 5-10 minutes.
    - Once the instance is Running, click on it and Stop it. This is extremely important such that it only runs during the training and you are not being overcharged.

5. Create the compute cluster for the training

    - On the top panel, next to Compute Instance, you will find and click **Compute Cluster**.
    - Click on **New > Next**
    - Type a cluster name like: `azutoml-cluster`
    - Set the maximum number of nodes to 2
    - Click on **Create**

You are ready for the course!!!

Estimated cost for the training: 5 hours * ( 0.29 USD/hour * 3 instances ) = USD 4.40


