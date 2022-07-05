cd client
printf "export const API_ROOT = \"http://3.65.42.31/api/\"" > src/api_root.js
npm run build
printf "export const API_ROOT = \"http://localhost:5000/api/\"" > src/api_root.js
cd ..
rm setup_files/public -r
rm setup_files/server -r
cp client/public setup_files/public -r
mkdir setup_files/server
cp server/*.sql server/*.py server/articles setup_files/server -r
zip -r setup_files.zip setup_files
printf "rm * -r" | VblogConn
VblogUpload setup_files.zip setup_files.zip
rm setup_files.zip
printf "unzip setup_files.zip; rm setup_files.zip; chmod +x setup_files/setup.sh; ./setup_files/setup.sh" | VblogConn
