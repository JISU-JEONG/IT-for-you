<template>
  <main id="app" class="content">
    <h1>내인생을 부탁해</h1>
    <nav class="nav">
      <menu class="nav__controls">
        <div
          v-for="(active, menu) in menus"
          class="nav__label"
          :class="{
          'nav__label--active' : active,
          'nav__label--filter': activeFilters[menu].length
        }"
          :key="menu+0"
          @click="setMenu(menu, active)"
        >{{ menu }}</div>
        <div class="nav__label nav__label--clear" @click="clearAllFilters">Clear all</div>
      </menu>
    </nav>

    <transition-group name="dropdown" tag="section" class="dropdown" :style="dropdown">
      <menu
        v-for="(options, filter) in filters"
        class="filters"
        v-show="menus[filter]"
        ref="menu"
        :key="filter+0"
      >
        <div v-if="filter === 'rating'" class="filters__rating">
          <output>
            <label>Minimum Level:&nbsp;</label>
            {{ parseFloat(filters.rating).toFixed(1) }}
          </output>

          <input
            v-model="filters.rating"
            class="filters__range"
            type="range"
            :min="rating.min"
            :max="rating.max"
            step="0.1"
          />
        </div>

        <template v-else>
          <li
            v-for="(active, option) in options"
            class="filters__item"
            :class="{ 'filters__item--active': active }"
            @click="setFilter(filter, option)"
            :key="option+0"
          >{{ option }}</li>
        </template>
      </menu>
    </transition-group>

    <transition-group name="company" tag="ul" class="content__list">
      <div class="company" v-for="company in list" :key="company.id">
        <div class="company__info">
          <h2 class="company__name">{{ company.name }}</h2>
          <blockquote class="company__slogan">{{ company.slogan }}</blockquote>
        </div>

        <ul class="company__details">
          <label class="company__label">Level</label>
          <p class="company__rating">{{ company.rating.toFixed(1) }}</p>
        </ul>
      </div>
    </transition-group>
  </main>
</template>

<script>
import * as question from "../QuestionData.js";
export default {
  name: "CategoryList",

  data() {
    return {
      modal: false,
      companies: [],
      dropdown: { height: 0 },
      rating: { min: 10, max: 0 },
      filters: { countries: {}, categories: {}, rating: 0 },
      menus: { countries: false, categories: false, rating: false }
    };
  },
  computed: {
    activeMenu() {
      return Object.keys(this.menus).reduce(
        ($$, set, i) => (this.menus[set] ? i : $$),
        -1
      );
    },
    list() {
      let { countries, categories } = this.activeFilters;
      return this.companies.filter(({ country, keywords, rating }) => {
        if (rating < this.filters.rating) return false;
        if (countries.length && !~countries.indexOf(country)) return false;
        return (
          !categories.length || categories.every(cat => ~keywords.indexOf(cat))
        );
      });
    },
    activeFilters() {
      let { countries, categories } = this.filters;
      return {
        countries: Object.keys(countries).filter(c => countries[c]),
        categories: Object.keys(categories).filter(c => categories[c]),
        rating:
          this.filters.rating > this.rating.min ? [this.filters.rating] : []
      };
    }
  },
  watch: {
    activeMenu(index, from) {
      if (index === from) return;
      this.$nextTick(() => {
        if (!this.$refs.menu || !this.$refs.menu[index]) {
          this.dropdown.height = 0;
        } else {
          this.dropdown.height = `${this.$refs.menu[index].clientHeight +
            16}px`;
        }
      });
    }
  },

  methods: {
    setFilter(filter, option) {
      if (filter === "countries") {
        this.filters[filter][option] = !this.filters[filter][option];
      } else {
        setTimeout(() => {
          this.clearFilter(filter, option, this.filters[filter][option]);
        }, 100);
      }
    },
    clearFilter(filter, except, active) {
      if (filter === "rating") {
        this.filters[filter] = this.rating.min;
      } else {
        Object.keys(this.filters[filter]).forEach(option => {
          this.filters[filter][option] = except === option && !active;
        });
      }
    },
    clearAllFilters() {
      Object.keys(this.filters).forEach(this.clearFilter);
    },
    setMenu(menu, active) {
      Object.keys(this.menus).forEach(tab => {
        this.menus[tab] = !active && tab === menu;
      });
    }
  },

  beforeMount() {
    // fetch("https://s3-us-west-2.amazonaws.com/s.cdpn.io/450744/mock-data.json")
    //   .then(response => {
    //     return response.json();
    //   })
    //   .then(companies => {
    //     this.companies = companies;
    //     companies.forEach(({ country, keywords, rating }) => {
    //       this.$set(this.filters.countries, country, false);
    //       if (this.rating.max < rating) this.rating.max = rating;
    //       if (this.rating.min > rating) {
    //         this.rating.min = rating;
    //         this.filters.rating = rating;
    //       }
    //       keywords.forEach(category => {
    //         this.$set(this.filters.categories, category, false);
    //       });
    //     });
    //   });

    this.companies = question.data();
    question.data().forEach(({ country, keywords, rating }) => {
      this.$set(this.filters.countries, country, false);
      if (this.rating.max < rating) this.rating.max = rating;
      if (this.rating.min > rating) {
        this.rating.min = rating;
        this.filters.rating = rating;
      }
      keywords.forEach(category => {
        this.$set(this.filters.categories, category, false);
      });
    });
  }
};
</script>

<style lang="scss" src="@/components/Question/Category/CategoryList.scss" scoped>
</style>