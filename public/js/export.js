// export.js - Export and Data Utilities
// Author: Akshat Reddy (SE24UARI032)

$(document).ready(function () {

    // Export chart as PNG image
    $('#export-btn').click(function () {
        var canvas = document.getElementById('mainChart');

        if (currentChart === null) {
            alert('No chart to export. Please load data first.');
            return;
        }

        // Create a temporary link element
        var link = document.createElement('a');
        link.download = 'chart-' + activeDataset + '-' + Date.now() + '.png';
        link.href = canvas.toDataURL('image/png');
        link.click();
    });

});
