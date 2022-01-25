const manipulatorC = {
    name: 'manipulator',
    template: `
    <h2>Manipulator</h2>

    <!--<span class="badge badge-dark" id="man_pa">På</span>
    <span class="badge badge-dark" id="man_av">Av</span>-->

    <div class="col container bg-dark text-white">
    
        <div class="row">
            <div class="col"> Motor 1:</div>
                <div class="col">
                    <div class="progress mx-auto" id="M1" data-value='0'>
                    <span class="progress-left">
                        <span class="progress-bar border-primary"></span>
                    </span>
                    <span class="progress-right">
                        <span class="progress-bar border-primary"></span>
                    </span>
                    <div class="progress-value w-100 h-100 rounded-circle d-flex align-items-center justify-content-center">
                        <div class="h7 font-weight-bold">76</div> <span>%</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col"> Motor 2:</div>
                <div class="col">
                    <div class="progress mx-auto" id="M2" data-value='0'>
                    <span class="progress-left">
                        <span class="progress-bar border-primary"></span>
                    </span>
                    <span class="progress-right">
                        <span class="progress-bar border-primary"></span>
                    </span>
                    <div class="progress-value w-100 h-100 rounded-circle d-flex align-items-center justify-content-center">
                        <div class="h7 font-weight-bold">76</div> <span>%</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="row">
            <div class="col"> Motor 3:</div>
                <div class="col">
                    <div class="progress mx-auto" id="M3" data-value='0'>
                        <span class="progress-left">
                            <span class="progress-bar border-primary"></span>
                        </span>
                        <span class="progress-right">
                            <span class="progress-bar border-primary"></span>
                        </span>
                        <div class="progress-value w-100 h-100 rounded-circle d-flex align-items-center justify-content-center">
                            <div class="h7 font-weight-bold">76</div><span>%</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col">Motor 4:</div>
                    <div class="col">
                        <div class="progress mx-auto" id="M4" data-value='0'>
                            <span class="progress-left">
                                <span class="progress-bar border-primary"></span>
                            </span>
                            <span class="progress-right">
                                <span class="progress-bar border-primary"></span>
                            </span>
                        <div class="progress-value w-100 h-100 rounded-circle d-flex align-items-center justify-content-center">
                    <div class="h7 font-weight-bold">76</div><span>%</span>
                </div>
            </div>

        </div>
    </div>
    </div>
    `,
    data: function() {
        return {

        };
    },
}