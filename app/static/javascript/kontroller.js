const kontrollerC = {
    name: 'kontroller',
    template: `
    <h2>Kontroller</h2>
    
    <div class="container">
        <input type="radio" class="btn-check " name="state" id="init" autocomplete="off">
        <label class="btn btn-outline-success btn-sm" for="init">På</label>
    
        <input type="radio" class="btn-check btn-sm" name="state" id="stop" autocomplete="off" checked>
        <label class="btn btn-outline-danger btn-sm" for="stop">Av</label>
    </div>
    
    
    <div class="container">
        <input type="radio" class="btn-check" name="manuell" id="manuell" autocomplete="off" checked>
        <label class="btn btn-outline-success btn-sm" for="manuell">Manuell</label>
    
        <input type="radio" class="btn-check " name="manuell" id="auto" autocomplete="off">
        <label class="btn btn-outline-warning btn-sm" for="auto">Auto</label>
    </div>
    
    
    <div class="container">
        <input type="radio" class="btn-check" name="modus" id="mode2" autocomplete="off" checked>
        <!--<label class="btn btn-outline-success btn-sm" for="mode2">Manipulator</label>-->
        <input type="radio" class="btn-check" name="modus" id="mode1" autocomplete="off">
    </div>
    `,
    data: function() {
        return {

        };
    },
}