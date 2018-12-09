<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Innra</title>
  </head>
  <body>
      <div>
          <h1>Aðgerðir</h1>
          <form action="/adgerd" method="post">
              <input type="checkbox" id="breyta" name="adgerdir" value="breyta">
              <label for="breyta">BREYTA FRÉTT</label>
              <input type="checkbox" id="eyda" name="adgerdir" value="eyda">
              <label for="eyda">EYÐA FRÉTT</label>
              <input type="checkbox" id="baeta" name="adgerdir" value="baeta">
              <label for="baeta">NÝ FRÉTT</label>
              <input value="Staðfesta" type="submit" />
          </form>
      </div>
  </body>
</html>