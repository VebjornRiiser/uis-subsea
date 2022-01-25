const bildebehandlingC = {
    props: ['bildebehandling'],
    name: 'bildebehandling',
    template: `
    <h2>Bildebehandling</h2>
    
    <div class="container">
        <button name="analyser_koralrev" type="button" class="btn btn-outline-success btn-sm">Korallrev</button>
        <span>Siste bilde analyseres.</span>
    </div>

    <div class="container">
        <button name="analyser_oversiktsbilde" type="button" class="btn btn-outline-success btn-sm">Havbunn</button>
        <span>Siste bilde analyseres.</span>
    </div>
    
    <div class="container">
        <button name="fotomosaikk" type="button" class="btn btn-outline-success btn-sm">Fotomosaikk</button>
        <span>Siste fem bilder analyseres.</span>
    </div>
    `,
    data: function() {
        return {

        };
    },
}