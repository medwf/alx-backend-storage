"CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
"https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
"SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
