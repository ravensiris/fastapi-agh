import axios from "axios";
import { useQuery } from "react-query";

export type User = {
    id: string;
    name: string;
    surname: string;
    age: number;
    email: string;
}

export const UserComponent = (user: User) => {
    return (
        <div>
            {user.name} {user.surname}, age {user.age}, email {user.email}
        </div>
    )
}

export const UserList = () => {
  const fetchUser = async () => {
    const { data } = await axios.get<User[]>(
      `http://localhost:8000/students`
    );
    return data;
  };
  const {
           isLoading,
           isSuccess,
           error,
           isError,
           data: userList
    } = useQuery({queryKey: ["user"], queryFn: fetchUser});
  return (
    <div>
      {isLoading && <article>...Loading users </article>}
      {isError && <article>{error.message}</article>}
      {isSuccess && (
          <article>
              {userList.map(user => <UserComponent key={user.name} {...user} />)}
          </article>
      )}
    </div>
  );
};
export default User;
