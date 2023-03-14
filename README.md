# Invoice Manager

Application was created to automate invoice managing process. Periodically, it sends requests to Etsy and eBay APIs to retrive orders data. 
If some orders occur the details are processed and added to MySQL database. Data of the orders without invoices are prepared to create invoice using ING Księgowość API. As a final step, created invoice is sent in a email message. 
