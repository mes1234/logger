# Documentation of logger tool
## Overview
This tool is used to log user work history and present it in easy to analyze way
## Python API
* __Projects__
  * End point : */projects*
  * Description : Endpoint to work with projects list
    * GET : list all currently stored projects in form:
    ```javascript
        {
            id:integer:
            {
                description: string,
                name: string
            }
        }
    ```
    * PUT : add new project, requires:
      * name : string
      * description : string
    * DELETE : remove project 
      * id : integer
    * UPDATE : update data for project :
      * id: integer
      * name : string
      * description  : string
* __Items__
  * Endpoint: /item
* Description : Endpoint to work with items in project
    * GET /item/<integer:project_id> : list all currently stored items in project in form:
    ```javascript
        {
            id:integer:
            {
                description: string,
                name: string
                date: date in format ??
            }
        }
    ```
    * PUT : add new item to project 
      * project_id : integer,
      * name : string
      * description : string
      * date : yyyy-mm-ddThh:mm
      * base_item_id : integer

* __SQL setup__
  * __projects table__: 
      * id: primary key
      * name: string
      * description: string
      * owner_id : foregin key -> users_table
      * users_id : TODO
  * __items table__: 
      * id: primary key
      * project_id : foregin key -> projects table
      * name: string
      * description: string
      * date : yyyy-mm-ddThh:mm
      * owner_id : foregin key -> users_table
  * __users table__: 
      * id: primary key
      * name: string
      * password: string<-shall be hash but it is TODO
      * root: boolean



