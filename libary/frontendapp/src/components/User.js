import React from "react";

const UserItem = ({user}) => {
   return (
       <tr>
           <td className="Line">
               {user.username}
           </td>
           <td className="Line">
               {user.first_name}
           </td>
           <td className="Line">
               {user.last_name}
           </td>
           <td className="Line">
               {user.email}
           </td>

       </tr>
   )
}

const UserList = ({users}) => {
    return (
        <body>
        <header class="header">
            <ul>
                    <li><a href="#">Главная</a></li>
                    <li><a href="#">Пользователи</a></li>
                </ul>
        </header>
            <div>
                <table class="Table">
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
        <footer class="footer">
            2021 CopyRight &copy;
        </footer>
        </body>
    )
}


export default UserList
