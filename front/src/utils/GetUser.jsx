import endpoints from './endpoint';
import fetcher from './Fetch';

export const getUsers = () => {
  let users = fetcher(`${endpoints}/api/user/getAll`);
  users.then(data => {
    console.log(data);
  });
  return users;
};