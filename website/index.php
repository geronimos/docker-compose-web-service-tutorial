<html>
    
    <head>
        <title>My lists</title>
    </head>

    <body>
        <h1>Welcome to my lists of favorites!</h1>
        
        <h2>Books<h2>
        <ul>
            <?php
                
                $json = file_get_contents("http://books-service");
                $obj = json_decode($json);

                $books = $obj->books;
                foreach ($books as $book) {
                    echo "<li>$book</li>";
                }
            ?>
        </ul>

        <h2>Fruits<h2>
        <ul>
            <?php

                $json = file_get_contents("http://fruits-service");
                $obj = json_decode($json);

                $fruits = $obj->fruits;
                foreach ($fruits as $fruit) {
                    echo "<li>$fruit</li>";
                }
            ?>
        </ul>

    </body>

</html>