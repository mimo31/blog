cd client
printf "export const API_ROOT = \"http://3.65.42.31/api/\"" > src/api_root.js
npm run build
printf "export const API_ROOT = \"http://localhost:5000/api/\"" > src/api_root.js
cd ..
rm package/public -r
rm package/server -r
cp client/public package/public -r
cp server/articles/article_resrcs package/public/article_resrcs -r
mkdir -p package/server/articles
cp server/*.sql server/*.py package/server -r
cp server/articles/*.html package/server/articles/
zip -r package.zip package
printf "ls | grep -xv \"blog\" | xargs rm -rf" | VblogConn
VblogUpload package.zip package.zip
rm package.zip
printf "unzip package.zip; rm package.zip; chmod +x package/setup.sh; ./package/setup.sh" | VblogConn
