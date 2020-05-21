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
        <div class="nav__label nav__label--clear" @click="clearAllFilters">랜덤문제 풀기</div>
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
        <div v-if="filter === '난이도'" class="filters__난이도">
          <output>
            <label>Minimum Level:&nbsp;</label>
            {{ parseFloat(filters.난이도).toFixed(1) }}
          </output>

          <input
            v-model="filters.난이도"
            class="filters__range"
            type="range"
            :min="난이도.min"
            :max="난이도.max"
            step="1"
          />
        </div>

        <template v-else>
          <div
            v-for="(active, option) in options"
            class="filters__item"
            :class="{ 'filters__item--active': active }"
            @click="setFilter(filter, option)"
            :key="option+0"
          >{{ option }}</div>
        </template>
      </menu>
    </transition-group>

    <transition-group name="company" tag="ul" class="content__list">
      <div
        class="company"
        v-for="company in list"
        :key="company.id"
        @click="questionDetail(company)"
      >
        <div class="company__info">
          <h2 class="company__name">{{ company.name }}</h2>
          <blockquote class="company__slogan">{{ questionType[company.slogan] }}</blockquote>
        </div>

        <ul class="company__details">
          <label class="company__label">Level</label>
          <p class="company__난이도">{{ company.난이도.toFixed(1) }}</p>
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
      난이도: { min: 10, max: 0 },
      filters: { 문제유형: {}, 카테고리: {}, 난이도: 0 },
      menus: { 문제유형: false, 카테고리: false, 난이도: false },
      questionType: ["OX퀴즈", "객관식", "주관식", "단답형", "녹음"]
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
      let { 문제유형, 카테고리 } = this.activeFilters;
      return this.companies.filter(({ country, keywords, 난이도 }) => {
        if (난이도 < this.filters.난이도) return false;
        if (문제유형.length && !~문제유형.indexOf(country)) return false;
        return (
          !카테고리.length || 카테고리.every(cat => ~keywords.indexOf(cat))
        );
      });
    },
    activeFilters() {
      let { 문제유형, 카테고리 } = this.filters;
      return {
        문제유형: Object.keys(문제유형).filter(c => 문제유형[c]),
        카테고리: Object.keys(카테고리).filter(c => 카테고리[c]),
        난이도:
          this.filters.난이도 > this.난이도.min ? [this.filters.난이도] : []
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
      if (filter === "문제유형") {
        this.filters[filter][option] = !this.filters[filter][option];
      } else {
        setTimeout(() => {
          this.clearFilter(filter, option, this.filters[filter][option]);
        }, 100);
      }
    },
    clearFilter(filter, except, active) {
      if (filter === "난이도") {
        this.filters[filter] = this.난이도.min;
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
    },
    questionDetail(company) {
      this.$store.dispatch("questionData", company);
      console.log(company);
      this.$router.push("/detail");
    }
  },

  beforeMount() {
    this.companies = question.data();
    question.data().forEach(({ country, keywords, 난이도 }) => {
      this.$set(this.filters.문제유형, country, false);
      if (this.난이도.max < 난이도) this.난이도.max = 난이도;
      if (this.난이도.min > 난이도) {
        this.난이도.min = 난이도;
        this.filters.난이도 = 난이도;
      }
      keywords.forEach(category => {
        this.$set(this.filters.카테고리, category, false);
      });
    });
  }
};
</script>

<style lang="scss" src="@/components/Question/Category/CategoryList.scss" scoped>
</style>