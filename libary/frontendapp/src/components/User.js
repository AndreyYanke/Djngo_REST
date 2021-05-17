import React from "react";

const UserItem = ({user}) => {
   return (
       <tr>
           <td>
               {user.first_name}
           </td>
           <td>
               {user.last_name}
           </td>
           <td>
               {user.email}
           </td>
       </tr>
   )
}

const UserList = ({users}) => {
   return (
       <div className="outer">
           <div className="header">
               <ul>
                   <li><a href="#">Главная</a></li>
                   <li><a href="#">О нас</a></li>
                   <li><a href="#">Галерея</a></li>
                   <li><a href="#">Контакты</a></li>
               </ul>
           </div>
           <div className="inner">
               <table className="Table">
                   <th>
                       User name
                   </th>
                   <th>
                       First name
                   </th>
                   <th>
                       Last Name
                   </th>
                   <th>
                       Email
                   </th>
                   {users.map((user) => <UserItem user={user}/>)}

               </table>
           </div>
           <div className="footer">

               <p>this footer</p>
           </div>

       </div>
   )
}


export default UserList
