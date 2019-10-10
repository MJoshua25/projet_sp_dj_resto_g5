var weekday = new Array(7);

weekday[1] = 1;
weekday[2] = 2;
weekday[3] = 3;
weekday[4] = 4;
weekday[5] = 5;
weekday[6] = 6;
weekday[0] = 7;

// Début Vue.js pour spécial

Vue.component('special-item-1', {
    props: ['plat', 'index'],
    template: `
        <div v-if="index % 2 ==0" class="row mt-5">
            <div class="col-lg-5 col-md-6 align-self-center py-5">
                <h2 class="special-number">`+"${ index + 1 }."+`</h2>
                <div class="dishes-text">
                    <h3><span>`+"${ plat.nom }"+`</span><br>`+"${ plat.ingredient }"+`</h3>
                    <p class="pt-3">`+"${ plat.description }"+`</p>
                    <h3 class="special-dishes-price">$`+"${ plat.prix }"+`</h3>
                    <a href="../reservation" class="btn-primary mt-3">book a table</a>
                </div>
            </div>
            <div class="col-lg-5 offset-lg-2 col-md-6 align-self-center mt-4 mt-md-0">
                <img v-bind:src="`+ "plat.image" + `" alt="" class="img-fluid shadow w-100">
            </div>
        </div>
        <div v-else class="row mt-5">
            <div class="col-lg-5 col-md-6 align-self-center order-2 order-md-1 mt-4 mt-md-0">
                <img v-bind:src="`+ "plat.image" + `" alt="" class="img-fluid shadow w-100">
            </div>
            <div class="col-lg-5 offset-lg-2 col-md-6 align-self-center order-1 order-md-2 py-5">
                <h2 class="special-number">`+"${ index + 1 }."+`</h2>
                <div class="dishes-text">
                <h3><span>`+"${ plat.nom }"+`</span><br>`+"${ plat.ingredient }"+`</h3>
                <p class="pt-3">`+"${ plat.description }"+`</p>
                <h3 class="special-dishes-price">$`+"${ plat.prix }"+`</h3>
                <a href="../reservation" class="btn-primary mt-3">book a table</a>
                </div>
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

// Fin Vue.js pour spécial


// Début Vue.js pour Menu



Vue.component('menu-item', {
    props: ['plat'],
    template: `
    <div class="menus d-flex align-items-center">
        <div class="menu-img rounded-circle">
            <img class="img-fluid" v-bind:src="`+ "plat.image" + `" alt="">
        </div>
        <div class="text-wrap">
            <div class="row align-items-start">
                <div class="col-8">
                    <h4>`+"${ plat.nom }"+`</h4>
                </div>
                <div class="col-4">
                    <h4 class="text-muted menu-price">$`+"${ plat.prix }"+`</h4>
                </div>
            </div>
            <p>`+"${ plat.ingredient }"+`</p>
        </div>
    </div>
    `,
    delimiters: ["${","}"],
})


Vue.component('category-menu-item', {
    props: ['category'],
    template: `
    <div class="heading-menu">
        <h3 class="text-center mb-5">`+"${ category.nom }"+`</h3>
    </div>
    <menu-item v-for="plat in category.plats" v-bind:plat="plat" v-bind:key="plat.id"></menu-item>
    `,
    delimiters: ["${","}"],
})


var menu = new Vue({
    el: '#gtco-menu',
    data: {
        loader: true,
        content:false,
        menu:[],
    },
    delimiters: ["${","}"],
    mounted(){
        this.get_menu()
    },
    methods: {
        get_menu: function(){
            axios.get('http://127.0.0.1:8000/api/menu/')
                .then(response => {
                    console.log(response.data)
                    this.loader=false
                    this.content=true
                    this.menu=response.data
                })
                .catch((err) => {
                    console.log(err);
                })
        }
    }
})


// Fin Vue.js pour menu



// Début Vue.js pour testimonial


Vue.component('testimonial-item', {
    props: ['testimonial'],
    template: `
    <div class="testi-item">
        <i class="testi-icon fa fa-3x fa-quote-left"></i>
        <p class="testi-text">`+"${ testimonial.commentaire }"+`</p>
        <p class="testi-author">`+"${ testimonial.nom }"+`</p>
        <p class="testi-desc">`+"${ testimonial.job }"+`</p>
    </div>
    `,
    delimiters: ["${","}"],
})


var testimonial = new Vue({
    el: '#gtco-testimonial',
    data: {
        loader: true,
        content:false,
        testimonials:[],
    },
    delimiters: ["${","}"],
    mounted(){
        this.get_testimonial()
    },
    methods: {
        get_testimonial: function(){
            axios.get('http://127.0.0.1:8000/api/temoignage/')
                .then(response => {
                    console.log(response.data)
                    this.loader=false
                    this.testimonials=response.data
                    this.content=true
                })
                .catch((err) => {
                    console.log(err);
                })
        }
    }
})


// Fin Vue.js pour testimonial


// Début Vue.js pour team


Vue.component('team-item', {
    props: ['team'],
    template: `
    <div class="col-md-4">
        <div class="team-card mb-5">
            <img class="img-fluid" v-bind:src="`+ "team.photo" + `" alt="">
            <div class="team-desc">
                <h4 class="mb-0">`+"${ team.prenom } ${ team.nom }"+`</h4>
                <p class="mb-1">`+"${ team.poste }"+`</p>
                <ul class="list-inline mb-0 team-social-links">
                    <li class="list-inline-item">
                        <a href="#">
                            <i class="fab fa-facebook-f"></i>
                        </a>
                    </li>
                    <li class="list-inline-item">
                        <a href="#">
                            <i class="fab fa-twitter"></i>
                        </a>
                    </li>
                    <li class="list-inline-item">
                        <a href="#">
                            <i class="fab fa-instagram"></i>
                        </a>
                    </li>
                    <li class="list-inline-item">
                        <a href="#">
                            <i class="fab fa-google-plus-g"></i>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    `,
    delimiters: ["${","}"],
})


var team = new Vue({
    el: '#gtco-team',
    data: {
        loader: true,
        content:false,
        teams:[],
    },
    delimiters: ["${","}"],
    mounted(){
        this.get_teams()
    },
    methods: {
        get_teams: function(){
            axios.get('http://127.0.0.1:8000/api/personnel/')
                .then(response => {
                    console.log(response.data)
                    this.loader=false
                    this.teams=response.data
                    this.content=true
                })
                .catch((err) => {
                    console.log(err);
                })
        }
    }
})


// Fin Vue.js pour team