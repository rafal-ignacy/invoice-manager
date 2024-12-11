# Invoice Manager

## Overview
Application was created to automate invoice managing process. Periodically, it sends requests to Etsy and eBay APIs to retrive orders data.  
Once an order is placed the details are processed and added to MySQL database. Based on stored order details as next step is creating an invoice with invoice management system API (ING Księgowość).  
As a final step, created invoices are sent in a email message.
Application is prepared to be easily deployed in a Docker container.

## Application workflow
```mermaid
graph LR
    subgraph orders_details [orders details]
        A[eBay API]
        B[Etsy API]
    end
    subgraph application_core [application core]
        C[orders processing]
        D[invoice processing]
    end
    A --> C
    B --> C
    C --> E[database]
    D --> E
    D --> F[Invoice management system API 
    ING Księgowość]
```