const kameraC = {
    name: 'kamera',
    template: `
    <h2>Kamera</h2>

    <div class="container">
        <button name="ta_bilde_frontkamera" type="button" class="btn btn-outline-success btn-sm">Ta bilde frontkamera</button>
    </div>

    <div classs="container">
        <button name="ta_bilde_havbunnKamera" type="button" class="btn btn-outline-success btn-sm">Ta bilde havbunnkamera</button>
    </div>

    <div class="container">
        <button name="ta_bilde_mROV" type="button" class="btn btn-outline-success btn-sm">Ta bilde mROV</button>
    </div>
    <div class="container">
        <button name="slett_siste_bilde" type="button" class="btn btn-outline-danger btn-sm">Slett det siste bildet</button>
    </div>

    <div class="container">
        <p>Resultatene kommer opp i egne faner</p>
    </div>
    `,
    data: function() {
        return {

        };
    },
}