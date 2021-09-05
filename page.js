var flashPlayers = ["adobeflash", "lightspark", "shumway", "awayfl", "ruffle", "gnash"];
var container = document.getElementById("flash-matrix");
var statsContainer = document.getElementById("stats");

function replaceNames(name) {
    return name.replace("adobeflash", "Adobe Flash").replace("awayfl", "AwayFL");
}

fetch('flash-matrix.json')
    .then(response => response.text())
    .then((data) => {
        var json = JSON.parse(data);
        var modifiedOn = json['modifiedOn'];
        var matrix = json['matrix'];

        document.getElementById('modifiedOn').innerHTML = "Last modified on " + modifiedOn;

        var statsTable = document.createElement("table");
        var featureTotalCount = 0;
        for (category in matrix) {
            for (feature in matrix[category]) {
                featureTotalCount++;
            }
        }

        for (player in flashPlayers) {
            var playerFeatureCount = 0;
            for (category in matrix) {
                for (feature in matrix[category]) {
                    if (matrix[category][feature][flashPlayers[player]] == "Yes") {
                        playerFeatureCount++;
                    }
                }
            }
            var playerStatsTr = document.createElement("tr");
            var playerName = document.createElement("td");
            playerName.innerHTML = replaceNames(flashPlayers[player]);
            var playerSupport = document.createElement("td");
            playerSupport.innerHTML = playerFeatureCount + " (" + (playerFeatureCount / 306 * 100).toFixed(2) + "%)";
            playerStatsTr.appendChild(playerName);
            playerStatsTr.appendChild(playerSupport);
            statsTable.appendChild(playerStatsTr);
        }
        statsContainer.appendChild(statsTable);

        for (var category in matrix) {
            var table = document.createElement("table");

            var header = document.createElement("tr");
            var blankHeaderItem = document.createElement("th");
            blankHeaderItem.innerHTML = "<strong>" + category + "</strong>";
            header.appendChild(blankHeaderItem);
            for (player in flashPlayers) {
                var playerTd = document.createElement("th");
                playerTd.innerHTML = replaceNames(flashPlayers[player]);
                header.appendChild(playerTd);
            }
            table.appendChild(header);

            for (feature in matrix[category]) {
                var tr = document.createElement("tr");

                var featureTd = document.createElement("td");

                var featureUrl = '<a class="featureUrl" href="https://help.adobe.com/en_US/FlashPlatform/reference/actionscript/3/flash/' + category + '/' + feature + '.html">' + feature + '</a>';
                featureTd.innerHTML = featureUrl;
                featureTd.style.width = "300px";
                tr.appendChild(featureTd);

                for (player in flashPlayers) {
                    var td = document.createElement("td");

                    var featureResult = matrix[category][feature][flashPlayers[player]];
                    td.innerHTML = featureResult;

                    if (featureResult == "Yes") {
                        td.style.backgroundColor = "green";
                    } else if (featureResult == "No") {
                        td.style.backgroundColor = "orange";
                    } else {
                        td.style.backgroundColor = "yellow";
                    }

                    tr.appendChild(td);
                }
                table.appendChild(tr);
            }

            container.appendChild(table);
            var breakLine = document.createElement("br");
            container.appendChild(breakLine);
        }
    });
