Vue.component('special-item-1', {
    props: ['plat'],
    template: `
            <div class="row mt-5">
                <div class="col-lg-5 col-md-6 align-self-center py-5">
                    <h2 class="special-number">01.</h2>
                    <div class="dishes-text">
                        <h3><span>`+"${ plat.nom }"+`</span><br>`+"${ plat.ingredient }"+`</h3>
                        <p class="pt-3">`+"${ plat.description }"+`</p>
                        <h3 class="special-dishes-price">$`+"${ plat.prix }"+`</h3>
                        <a href="#" class="btn-primary mt-3">book a table</a>
                    </div>
                </div>
                <div class="col-lg-5 offset-lg-2 col-md-6 align-self-center mt-4 mt-md-0">
                    <img v-bind:src="`+ "plat.image" + `" alt="" class="img-fluid shadow w-100">
                </div>
            </div>
    `,
    delimiters: ["${","}"],
})

Vue.component('special-item-2', {
    props: ['plat'],
    template: `
    <div class="row mt-5">
        <div class="col-lg-5 col-md-6 align-self-center order-2 order-md-1 mt-4 mt-md-0">
            <img src="img/salmon-zucchini.jpg" alt="" class="img-fluid shadow w-100">
        </div>
        <div class="col-lg-5 offset-lg-2 col-md-6 align-self-center order-1 order-md-2 py-5">
            <h2 class="special-number">02.</h2>
            <div class="dishes-text">
                <h3><span>Salmon</span><br> Zucchini</h3>
                <p class="pt-3">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis, accusamus culpa quam amet ipsam odit ea doloremque accusantium quo, itaque possimus eius. In a quis quibusdam omnis atque vero dolores!</p>
                <h3 class="special-dishes-price">$12.00</h3>
                <a href="#" class="btn-primary mt-3">book a table <span><i class="fa fa-long-arrow-right"></i></span></a>
            </div>
        </div>
    </div>
    `,
    delimiters: ["${","}"],
})

var special = new Vue({
    el: '#gtco-special-dishes',
    data: {
        loader: true,
        content:false,
        plats:[],
    },
    delimiters: ["${","}"],
    mounted(){
        //this.hello();
        this.get_plat()
    },
    methods: {
        get_plat: function(){
            axios.get('http://127.0.0.1:8000/api/plat/')
                .then(response => {
                    console.log(response.data)
                    this.loader=false
                    this.content=true
                    this.plats=response.data
                })
                .catch((err) => {
                    console.log(err);
                })
        }
    }
})