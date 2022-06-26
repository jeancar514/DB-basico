/* crear db*/
create database prueba ; 
/* permitir manipular la db*/
use prueba; 
/* botar la db*/
drop database prueba ;
/* crear una tabla*/
create table Usuario(id int, email varchar(100),username varchar(50)); 
/* agregar una columna*/
alter table Usuario add edad int;
/* eliminar */
alter table Usuario drop column edad;
/* modificar una columna */
alter table Usuario modify column email varchar(50);
/* insertar datos */
insert into Usuario(email,username, edad)
values('leonela@gmail.com','leonela','18');

delete from Usuario where email = "jeancarleonardo514@gmail.com"  limit 1;

alter table Usuario add primary key(id);

alter table Usuario modify column id int auto_increment; 

select * from Usuario;

select * from Usuario where email = 'jeison@gmail.com' ;

select * from Usuario where edad > 19;

update Usuario set edad = 23 where id = 1;

update Usuario set edad = 23 ;

delete from Usuario where id = 1;

