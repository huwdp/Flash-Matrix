import './App.css';
import { useState, useEffect } from 'react';

// TODO: Run JSLint
// TODO: Warning: Each child in a list should have a unique "key" prop.
// TODO: Possibly use Reducer

const flashTotalClassCount = 306;

function replaceNames(name) {
    return name.replace("adobeflash", "Adobe Flash").replace("awayfl", "AwayFL");
}

function buildStatsData(players, matrix) {
  let output = [];
  for (const player in players) {
      const name = players[player];
      let playerFeatureCount = 0; // TODO: Rename this
      let playerFeatureIncludingPartialCount = 0; // TODO: Rename this
      for (const category in matrix) {
          for (const feature in matrix[category]) {
              if (matrix[category][feature][players[player]] === "Yes") {
                  playerFeatureCount++;
                  playerFeatureIncludingPartialCount++;
              }
              if (matrix[category][feature][players[player]] === "Partially") {
                  playerFeatureIncludingPartialCount++;
              }
          }
      }
      output.push({
        "name": name,
        "featureCount": playerFeatureCount,
        "allFeatureCount": playerFeatureIncludingPartialCount
      });
  }
  return output;
}

export default function App() {
  let [modifiedOn, setModifiedOn] = useState("");
  let [matrix, setMatrix] = useState({});
  // TODO: Add ids to lists

  const [players, setPlayers] = useState([
    "adobeflash",
    "lightspark",
    "ruffle",
    "shumway",
    "awayfl",
    "gnash"
  ]);
  let [stats, setStats] = useState([]);
  useEffect(() => {
    fetch('flash-matrix.json')
      .then(response => response.text())
      .then((data) => {
          let json = JSON.parse(data);
          setModifiedOn(json['modifiedOn']);
          setMatrix(json['matrix']);
          setStats(buildStatsData(players, json['matrix']));
        });
  }, [players]);
  return (
    <div id="container">
      <Header/>
      <FlashStats players={players} stats={stats}/>
      <FlashMatrixTables players={players} matrix={matrix}/>
      <Footer modifiedOn={modifiedOn}/>
    </div>
  );
}

function Header()
{
  return (
    <>
    <h1>Flash Player Matrix</h1>
    <p>The matrix gives approximate support of <a href="https://mozilla.github.io/shumway/">Shumway</a>, <a href="https://lightspark.github.io/">Lightspark</a>, <a href="https://www.gnu.org/software/gnash/">Gnash</a>, <a href="https://ruffle.rs/">Ruffle</a> and <a href="https://awayfl.org/">AwayFL</a> flash players compared the defacto standard Adobe Flash Player. <i>The matrix is not 100% correct due to the difficulty in measuring API support within the source code of each Flash Player.</i>
  </p>
  <p>Adobe Flash support ended on December 31, 2020. Click <a href="https://www.adobe.com/products/flashplayer/end-of-life.html#">here</a> for information about the end of life support.</p>
  </>
  );
}

function FlashStats({players, stats})
{
  return (
    <>
    <h2>Flash players</h2>
    <table>
    <tbody>
      <tr><th>Flash player</th><th>AS3 API Implementation</th><th>AS3 API Implementation (including partial ones)</th></tr>
      {stats.map(row =>
        <tr>
          <td>{replaceNames(row.name)}</td>
          <td>{row.featureCount} ({Number(row.featureCount/flashTotalClassCount*100).toFixed(2)}%)</td>
          <td>{row.allFeatureCount} ({Number(row.allFeatureCount/flashTotalClassCount*100).toFixed(2)}%)</td>
        </tr>
      )}
      </tbody>
    </table>
    </>
  );
}

function FlashMatrixTables({players, matrix})
{
    return (
      <div id="flash-matrix">
        <h2>AS3 implementation support matrix</h2>
        {Object.keys(matrix).map(namespaceName =>
          <FlashMatrixTable namespaceName={namespaceName} players={players} matrix={matrix}/>
        )}
      </div>
    )
}

function FlashMatrixTable({namespaceName, players, matrix})
{
  return (
    <div>
    <table>
      <thead>
        <tr>
          <th>{namespaceName}</th>
          {players.map(player =>
            <th>{replaceNames(player)}</th>
          )}
        </tr>
      </thead>
      <tbody>
        {Object.keys(matrix[namespaceName]).map(className =>
          <FlashMatrixTableLine namespaceName={namespaceName} className={className} players={players} matrix={matrix}/>
        )}
      </tbody>
    </table>
    <br />
    </div>
  );
}

function FlashMatrixTableLine({namespaceName, className, players, matrix})
{
  const url = 'https://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/' + namespaceName + '/' + className + '.html';
  return (
    <tr>
      <td className="featureName"><a className="featureUrl" href={url}>{className}</a></td>
      {players.map(player =>
        <FlashMatrixTableLineCell text={matrix[namespaceName][className][player]} />
      )}
    </tr>
  );
}

function FlashMatrixTableLineCell({text})
{
  if (text === "Yes")
  {
    return (
      <td className="green-bg">{text}</td>
    );
  }
  if (text === "Partially")
  {
    return (
      <td className="yellow-bg">{text}</td>
    );
  }
  return (
    <td className="orange-bg">{text}</td>
  );
}

function Footer({modifiedOn}) {
  return (
    <>
      <p id="modifiedOn">Last modified on {modifiedOn}</p>
    </>
  );
}
