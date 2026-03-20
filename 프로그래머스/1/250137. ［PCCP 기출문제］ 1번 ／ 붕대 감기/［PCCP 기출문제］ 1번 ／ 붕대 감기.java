class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        
        int totalRounds = attacks[attacks.length-1][0];
        int attackIdx = 0;
        
        int bandageCoolDown = bandage[0];
        int HealPerSec = bandage[1];
        int bonusHeal = bandage[2];
        
        int curHealth = health;
        int curSuccess = 0;
        for(int i=1; i<=totalRounds; i++) {
           
            // 공격받을 때
            if(attackIdx < attacks.length && i == attacks[attackIdx][0]) {
                curHealth -= attacks[attackIdx][1];
                curSuccess = 0;
                attackIdx++;
                
                if(curHealth <= 0) {
                    return -1;
                }
                // System.out.println(i + "번째: " + curHealth + ", " + curSuccess + ", " + (i == attacks[attackIdx][0]) + "attkIdx: " + attackIdx);
                continue;
            }
            // 공격받지 않고, 최대체력 아닐때
            curSuccess++;
            curHealth = Math.min(health, curHealth += HealPerSec);
            
            // 공격받지 않고, 연속 성공 max일 때
            if(bandageCoolDown == curSuccess) {
                curSuccess = 0;
                if(health != curHealth) {
                    curHealth = Math.min(health, curHealth += bonusHeal);
                }
            }
            
            
             // System.out.println(i + "번째: " + curHealth + ", " + curSuccess + ", " + (i == attacks[attackIdx][0]) + "attkIdx: " + attackIdx);
        }
        
        answer = curHealth;
        return answer;
    }
}