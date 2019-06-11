import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Homepage.vue'
import Elems from './views/Elements.vue'
import Element from './views/Element.vue'
import Mols from './views/Molecules.vue'
import Molecule from './views/Molecule.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: "/elements",
      name: "elements",
      component: Elems
    },
    {
      path: '/elements/:id',
      name: 'element',
      component: Element
    },
    {
      path: "/molecules",
      name: "molecules",
      component: Mols
    },
    {
      path: '/molecules/:id',
      name: 'molecule',
      component: Molecule
    }
  ]
})
