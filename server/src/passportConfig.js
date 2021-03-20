const LocalStrategy = require('passport-local').Strategy;
const { Client } = require("pg")
<<<<<<< HEAD
const user = process.argv[2] == "local" ? "goeku" : "goeku"
const password = process.argv[2] == "local" ? undefined : "goeku"
=======
const user = process.argv[2] == "local" ? "goeku" : "postgres"
const password = process.argv[2] == "local" ? undefined : "postgres"
>>>>>>> a2ad6dda6a2c4286ed35593c95872c94afb07b50
const client = new Client({
    user,
    host: 'localhost',
    database: 'instabot',
    password,
    port: 5432,
});
client.connect();

const bcrypt = require('bcrypt');

function initialize (passport){
    const authenticateUser = (email, password, done) => {
        client.query(
            'SELECT * FROM clients WHERE email = $1', 
            [email],
            (err, results) => {
                if (err){
                    throw err;
                }

                console.log(results.rows);

                if (results.rows.length > 0){
                    const user = results.rows[0];

                    bcrypt.compare(password, user.password, (err, isMatch) => {
                        if(err){
                            throw err;
                        }

                        if(isMatch){
                            return done(null, user);
                        }else{
                            return done(null, false, {message: "Şifre doğru değil."});
                        }
                    });
                }else{
                    return done(null, false, {message: "Email kayıtlı değil."});
                }
            }
        )
    }
    passport.use(
        new LocalStrategy(
            {
                usernameField: "email",
                passwordField: "password"
            }, 
            authenticateUser
        )
    );

    passport.serializeUser((user, done) => done(null, user.id));
    passport.deserializeUser((id, done) => {
        client.query(
            'SELECT * FROM clients WHERE id = $1', [id], (err, results) => {
                if(err){
                    throw err;
                }
                return done(null, results.rows[0]);
            });
    });
}

module.exports = initialize;