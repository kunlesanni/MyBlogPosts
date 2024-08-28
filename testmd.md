---
title: Simplifying Terraform State Management - The GUI way 💎
published: true
description: A comprehensive guide on simplifying Terraform state management using Terraform Cloud. 
tags: 'terraform, tfstate, TerraformCloud, azure, iac'
cover_image: 'https://raw.githubusercontent.com/kunlesanni/MyBlogPosts/main/2024/june/TerraformStateWithTFC/images/tfdod.JPG'
canonical_url: null
id: 001
series: 
date: 2024-06-18 22:00 +0000
---
###### TL;DR

* *Terraform Cloud Workspaces simplify state management and enhance collaboration and version control through an intuitive GUI.*
* *Terraform state is a snapshot of infrastructure at a given point in time, mapping Terraform configurations to real-world resources.*
* *Traditional state management approaches, such as storing state files locally or on a shared file system, can lead to issues like corruption, merge conflicts, and state drift.*
* *Terraform Cloud Workspaces offer a centralized solution by storing state files in the cloud, providing access to the latest version of the state and state locking to prevent conflicts.*
* *It also allows for versioning infrastructure and provides an easy-to-use GUI for managing resources with features like state locking, versioning, and a user-friendly interface.*
* *Terraform Cloud Workspaces streamline infrastructure management and make it more accessible, easy to restore different versions of you infrastructure, plus its free to get started. 😄*

#### Overview

Formula D, a car racing motorsport is such a thrill to watch for most folks, even if you are not a fan. It involves not just getting across the finish line but also scoring points in the process by drifting plus a mix of driving styles.

With Terraform, a widely used Infrastructure as Code(IaC) tool, experiencing 'drift' is far from enjoyable, hence the ominous phrase 'TERRAFORM DRIFT OF DEATH'.

In the realm of Infrastructure as Code (IaC), managing the state of your infrastructure is as vital as the infrastructure itself. This post brings exciting news that makes using and managing Terraform not just essential, but also enjoyable.

Terraform employs a concept known as "state" to track the resources it manages. This state is a text file, auto-created from your Terraform configuration during the initial run, and stored within your workspace. As your configuration evolves, so does the state, providing an accurate representation of your actual infrastructure.

Terraform Cloud has a feature that not only revolutionizes state management, but also simplifies, enhances collaboration and version control, all through an intuitive GUI. This article delves deeper into this game-changing feature.

#### Understanding Terraform State

As explained above, Terraform state is a snapshot of your infrastructure at a given point in time. It maps your Terraform configurations to the actual resources, ensuring that Terraform knows what it is managing and how to update those resources without causing conflicts or duplications.

The state file is a file that stores your terraform state as text. By default, this file is saved on the file system of the host where Terraform is running.

It's crucial to keep this state file synchronized with your actual infrastructure. If they fall out of sync, you'll encounter discrepancies, also known as state drift.

#### The Pain of State Management

###### Local State

Traditionally, Terraform stores state files locally. While this approach works well for individual use, but it can quickly become a bottleneck for teams. Issues such as state file corruption, merge conflicts, and the dreaded "state drift" (where the state file no longer accurately reflects the actual infrastructure) can occur.

Since the state is stored on the host system's file system, collaboration becomes challenging. Each user ends up with a different copy of the state file, leading to inconsistencies. This approach is mostly recommended for local experimentation.

However, as your infrastructure and team grow, managing this state file can become increasingly complex due to frequent merge conflicts and drifts.

These limitations of using local storage led to the development of remote state management.

##### Remote State

As the name suggests, the state files are not stored locally, rather in a remote location where users can have access effectiveely share the same statefile of the infrastructure. This can be an AWS s3 bucket or an Azure storage account.

This is very effective for collaborative state management, but also has its own limitations.

This also comes with its own limitations,

(3) Here is a good terraform series by .........

(3) Here is a good Terraform series by [Olakunle Sanni](https://dev.to/kunlesanni).

{% user kunlesanni %}
