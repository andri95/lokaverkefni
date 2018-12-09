<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Forsíða</title>
  </head>
  <body>
      <h1>Stuttfréttir</h1>
      <div>
        % for x in frettir:
            % for key, value in x.items():
                <p>{{value}}</p>
            % end
        % end
      </div>
      <div>
        <ul>
           <a href="/login">Innskráning</a>
        </ul>
      </div>
  </body>
</html>
