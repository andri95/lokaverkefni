<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link type="text/css" href="/static/style.css" rel="stylesheet"/>
    <title>Forsíða</title>
  </head>
  <body>
      <div>
         <img src="/static/Stundin_logo.jpg" alt="Bottle">
      </div>
      <fieldset>
        % for x in frettir:
            % for key, value in x.items():
                <p>{{value}}</p>
            % end
        % end
      </fieldset>
      <div>
        <ul>
           <a href="/login">Innskráning</a>
        </ul>
      </div>
      % include('footer.tpl')
  </body>
</html>
