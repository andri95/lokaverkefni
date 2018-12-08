<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Forsíða</title>
  </head>
  <body>
    % for x in frettir:
        % for key, value in x.items():
            <p>{{value}}</p>
    <p>Frettir:  {{ frettir }} </p>
  </body>
</html>
