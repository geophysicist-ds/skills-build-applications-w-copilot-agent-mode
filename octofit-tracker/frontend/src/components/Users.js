import React, { useEffect, useState } from 'react';


const Users = () => {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
    console.log('Fetching Users from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setUsers(results);
        console.log('Users data:', results);
      })
      .catch(err => console.error('Error fetching users:', err));
  }, []);

  return (
    <div className="card shadow mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Users</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-dark">
              <tr>
                {users.length > 0 && Object.keys(users[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {users.map((user, idx) => (
                <tr key={idx}>
                  {Object.values(user).map((value, i) => (
                    <td key={i}>{typeof value === 'object' ? JSON.stringify(value) : value}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
export default Users;
