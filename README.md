# Invoice Manager

Application was created to automate invoice managing process. Periodically, it sends requests to Etsy and eBay APIs to retrive orders data. 
If some orders occur the details are processed and added to MySQL database. Data of the orders without invoices are prepared to create invoice using ING Księgowość API. As a final step, created invoices are sent in a email message.
Application is prepared to run in a Docker container.
