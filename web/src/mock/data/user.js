import Mock from 'mockjs';
const LoginUsers = [
  {
    id: 1,
    username: 'admin',
    password: '123456',
    avatar: 'https://raw.githubusercontent.com/taylorchen709/markdown-images/master/vueadmin/user.png',
    name: '张某某'
  }
];

const Users = [];

for (let i = 0; i < 86; i++) {
  Users.push(Mock.mock({
    version: Mock.Random.guid().substr(0,7),
    name: Mock.Random.cname(),
    status: Mock.Random.province(),
    role: Mock.Random.cword(),
    age: Mock.Random.integer(0, 1)
  }));
}

export { LoginUsers, Users };
