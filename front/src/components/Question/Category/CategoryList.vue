<template>
  <main id="app" class="content">
    <h1>내인생을 부탁해</h1>
    <nav class="nav">
      <menu class="nav__controls">
        <div
          v-for="(active, menu) in menus"
          class="nav__label"
          :class="{
            'nav__label--active': active,
            'nav__label--filter': activeFilters[menu].length
          }"
          :key="menu + 0"
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
        :key="filter + 0"
      >
        <div v-if="filter === 'level'" class="filters__level">
          <output>
            <label>Minimum Level:&nbsp;</label>
            {{ parseFloat(filters.level).toFixed(1) }}
          </output>

          <input
            v-model="filters.level"
            class="filters__range"
            type="range"
            :min="level.min"
            :max="level.max"
            step="1"
          />
        </div>

        <template v-else>
          <div
            v-for="(active, option) in options"
            class="filters__item"
            :class="{ 'filters__item--active': active }"
            @click="setFilter(filter, option)"
            :key="option + 0"
          >{{ option }}</div>
        </template>
      </menu>
    </transition-group>

    <transition-group name="question" tag="ul" class="content__list">
      <div class="question" v-for="question in list" :key="question.p_id">
        <div class="question__info">
          <h2 class="question__name">{{ question.p_question }}</h2>
          <blockquote class="question__slogan">{{ questionType[question.pt_id] }}</blockquote>
        </div>

        <ul class="question__details">
          <label class="question__label">Level</label>
          <p class="question__level">{{ question.pd_id }}</p>
        </ul>
      </div>
    </transition-group>

    <button @click="questionDetail()">문제 풀러 가기</button>
  </main>
</template>

<script>
import axios from "@/api/api.service.js";

export default {
  name: "CategoryList",
  data() {
    return {
      questionType: [],
      questionData: [],
      questionCategory: [],
      level: { min: Infinity, max: 0 },
      filters: { type: {}, category: {}, level: 0 },
      menus: { type: false, category: false, level: false },
      dropdown: { height: 0 }
    };
  },
  computed: {
    activeFilters() {
      let { type, category } = this.filters;
      return {
        type: Object.keys(type).filter(c => type[c]),
        category: Object.keys(category).filter(c => category[c]),
        level: this.filters.level > this.level.min ? [this.filters.level] : []
      };
    },

    activeMenu() {
      return Object.keys(this.menus).reduce(
        ($$, set, i) => (this.menus[set] ? i : $$),
        -1
      );
    },

    list() {
      let { type, category } = this.activeFilters;
      return this.questionData.filter(({ pt_id, pc_id, pd_id }) => {
        if (pd_id < this.filters.level) return false;
        if (type.length && !~type.indexOf(this.questionType[pt_id]))
          return false;
        return (
          !category.length ||
          category.every(cat => ~this.questionCategory[pc_id].indexOf(cat))
        );
      });
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
    clearFilter(filter, except, active) {
      if (filter === "level") {
        this.filters[filter] = this.level.min;
      } else {
        Object.keys(this.filters[filter]).forEach(option => {
          this.filters[filter][option] = except === option && !active;
        });
      }
    },

    setFilter(filter, option) {
      if (filter === "type") {
        this.filters[filter][option] = !this.filters[filter][option];
      } else {
        setTimeout(() => {
          this.clearFilter(filter, option, this.filters[filter][option]);
        }, 100);
      }
    },

    questionDetail() {
      let questionlist = this.list;

      let index = 0;
      this.list.forEach(({ answers }, i) => {
        answers.forEach(({ a_value, a_correct }, j) => {
          if (a_correct) {
            if (questionlist[i].currentAnswer === undefined) {
              questionlist[i].currentAnswer = [a_value];
            } else {
              questionlist[i].currentAnswer.push(a_value);
            }
            questionlist[i].currentIndex = index + j;
          }
        });

        index += answers.length;
      });
      this.$store.dispatch("questionList", questionlist);
      this.$store.dispatch("questionType", this.questionType);
      this.$store.dispatch("questionCategory", this.questionCategory);
      this.$router.push("/detail");
    },

    clearAllFilters() {
      Object.keys(this.filters).forEach(this.clearFilter);
    },

    setMenu(menu, active) {
      Object.keys(this.menus).forEach(tab => {
        this.menus[tab] = !active && tab === menu;
      });
    },

    async init() {
      // Category Get
      await axios.get("/api/problems/prob_cate/").then(({ data }) => {
        data.forEach(({ pc_id, pc_value }) => {
          this.$set(this.questionCategory, pc_id, pc_value);
        });
      });

      // Type Get
      await axios.get("/api/problems/prob_type/").then(({ data }) => {
        data.forEach(({ pt_id, pt_value }) => {
          this.$set(this.questionType, pt_id, pt_value);
        });
      });

      // Problems Get
      await axios.get("/api/problems/probs/").then(({ data }) => {
        this.questionData = data;
        data.forEach(({ pt_id, pc_id, pd_id }) => {
          // Type, Category
          this.$set(this.filters.type, this.questionType[pt_id], false);
          this.$set(this.filters.category, this.questionCategory[pc_id], false);
          // Level
          if (this.level.max < pd_id) this.level.max = pd_id;
          if (this.level.min > pd_id) {
            this.level.min = pd_id;
            this.filters.level = pd_id;
          }
        });
      });
    }
  },

  beforeMount() {
    this.init();
  }
};
</script>

<style
  lang="scss"
  src="@/components/Question/Category/CategoryList.scss"
  scoped
></style>
