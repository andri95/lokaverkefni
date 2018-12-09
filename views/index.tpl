<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Forsíða</title>
  </head>
  <body>
      <div>
        % for x in frettir:
            % for key, value in x.items():
                <p>{{value}}</p>
        % end
      </div>
      <div>
        <a href="/login">Innskráning</a>
      </div>
  </body>
</html>
