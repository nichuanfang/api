# vercel api 项目

> 关于在 linux 上执行`turso auth login`获取不到 Turso 的 token 的解决方案:

- Click on the link - ok
- Login on the web - ok
- Wait for browser to be redirected and 404 and then copy link
- Open another SSH connection to my Linux server
- Run wget -O /dev/null <http://localhost:PORT/?jwt=TOKEN&username=USERNAME> - so that the authentication process completes.
