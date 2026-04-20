#include <bits/stdc++.h>
using namespace std;

// bandage_len은 배열 bandage의 길이입니다.
// attacks_rows는 2차원 배열 attacks의 행 길이, attacks_cols는 2차원 배열 attacks의 열 길이입니다.

// bandage[0] = 시전시간
// bandage[1] = 초당 회복량
// bandage[2] = 추가 회복량

// attacks[0] = 공격시간
// attacks[1] = 피해량

bool beAttacked(int current_idx, int **attacks, int attack_idx) { return current_idx == attacks[attack_idx][0]; }

int heal(int max_health, int health, int healAmount) {
    if (health + healAmount >= max_health) {
        return max_health;
    }
    return health + healAmount;
}

int solution(int bandage[], size_t bandage_len, int health, int **attacks, size_t attacks_rows, size_t attacks_cols) {
    int final_attack_time = attacks[attacks_rows - 1][0];
    int heal_success_count = 0;
    int attack_idx = 0;
    int max_health = health;

    for (int i = 1; i <= final_attack_time; i++) {
        if (health < 0 || attack_idx == attacks_rows) {
            break;
        }
        // 시전시간동안 공격을 받으면 health에서 피해량 빼고 연속성공=0
        if (beAttacked(i, attacks, attack_idx)) {
            health -= attacks[attack_idx][1];
            attack_idx++;
            heal_success_count = 0;
            continue;
        }
        // 시전시간동안 공격을 받지 않으면 회복량만큼 회복

        health = heal(max_health, health, bandage[1]);
        heal_success_count++;

        if (heal_success_count == bandage[0]) {
            health = heal(max_health, health, bandage[2]);
            heal_success_count = 0;
            continue;
        }
    }

    if (health <= 0) {
        return -1;
    }
    return health;
}
