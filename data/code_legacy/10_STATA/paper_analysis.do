/*
PROJECT ALGORITHM

treat: 0 = punishment (Baseline condition), 1 = no punishment (Treatment condition)
*/

*ssc install estout, replace
frame create playerA
frame create playerB

frame change playerA
import excel using "../../processed_data/04_delegator/delegator_cleaned.xlsx", firstrow clear

frame change playerB
import excel using "../../processed_data/05_evaluator/evaluator_cleaned.xlsx", firstrow clear

********************************************************************************
********************************************************************************
**# Player A
********************************************************************************
********************************************************************************
frame change playerA

	****************************************************************************
	**# Experiment descriptives
	****************************************************************************

	*number of player A
	count //161
	
	*time spent
	sum time_taken //746sec = 12.43min
	
	*earnings
	
	*balance across observables
	local vars age female socio_status went_to_uni technology_score leader
	estpost ttest `vars', by(treat)

	esttab, ///
		cells("mu_1(fmt(3)) mu_2(fmt(3)) p(fmt(3))") ///
		collabels("Mean (treat=0)" "Mean (treat=1)" "p-value") ///
		label replace

	****************************************************************************
	**# Delegation behavior of Player A
	****************************************************************************
	
	*share of delegated decisions
	bys treat: sum delegation
	
	*Chi-squared test and Fisher exact test
	tab treat delegation, chi2
	tab treat delegation, exact
	
		*does this treatment difference vary when excluding people that did not pass attention check? answer: no, it is robust
		bys treat: sum delegation if pass_att1
		bys treat: sum delegation if pass_att2
		bys treat: sum delegation if pass_att1 & pass_att2
[check what random_order_del=1 implies]		
		*are there order effects? answer: yes, in the Baseline condition
		bys treat random_order_del: sum delegation
	
	****************************************************************************
	**# Explanation I: Beliefs
	****************************************************************************
	
	****************************************************************************
	**# Explanation II: Performance
	****************************************************************************
	*Does prospect of punishment exert more effort in people? answer: No, because among those that did not delegate, if no punishment is possible performance is better than if punishment was possible. 
	bys treat: sum success_last if delegation==0
	
	*But, maybe they already performed better before?
	bys treat: sum overall_score if delegation==0
	
	*Maybe there was improvement when looking at the continuous performance measure? The last task could have simply been easier. But then both groups should have improved equally. There are two outliers in true_performance, so I test on medians, not means
	gen improvement = abs(true_performance/10 - (guess_last - truth_last))
	bys treat: sum improvement if delegation==0, d
	signrank improvement = 0 if delegation==0 & treat==0
	signrank improvement = 0 if delegation==0 & treat==1
	
	*Is performance related to the delegation decision?
	preserve
		collapse (sum) delegation (count) test_slider, by(overall_score treat)
		rename test_slider count
		gen del_share = delegation/count
		
		twoway ///
			(scatter del_share overall_score [w=count] if treat==0, msymbol(O) mcolor(blue)) ///
			(line del_share overall_score [w=count] if treat==0, lcolor(blue)) ///
			(scatter del_share overall_score [w=count] if treat==1, msymbol(O) mcolor(red)) ///
			(line del_share overall_score [w=count] if treat==1, lcolor(red)), ///
			legend(off)
			ytitle("Delegation share") ///
			xtitle("Overall score")
	restore
	
	****************************************************************************
	**# Regressions
	****************************************************************************
	*baseline
	logit delegation treat
	logit delegation treat random_order_del //order effect similarly strong in both treatments
	
	*performance/beliefs about performance/difficulty/overconfidence
	pwcorr delegation overall_score if treat==0, sig
	pwcorr delegation overall_score if treat==1, sig
	logit delegation treat overall_score //actual performance
	logit delegation treat wa_confidence //beliefs about performance (weighted average)
	logit delegation treat highest_confidence //beliefs about performance (mode score)
	logit delegation treat overconfidence //overconfidence
	logit delegation treat wa_difficulty //difficulty
	
	logit delegation i.treat##c.overall_score //for interpretability I should rescale overall_score around its average
	sum overall_score
	gen overall_score_norm = overall_score - r(mean)
	
	logit delegation i.treat##c.overall_score_norm
	
	*with controls (across treatments)
	logit delegation treat overall_score age female socio_status went_to_uni technology_score leader
	logit delegation treat wa_confidence age female socio_status went_to_uni technology_score leader
	
	
	
	
	
	
	
	
********************************************************************************
********************************************************************************
**# Player B
********************************************************************************
********************************************************************************
frame change playerB

**# Experiment descriptives

	*number of player B
	count //161
	
	*time spent
	sum time_taken //474s = 7.9min
	
	*earnings
	
	*balance across observables
	local vars age female socio_status went_to_uni technology_score leader
	estpost ttest `vars', by(treat)

	esttab, ///
		cells("mu_1(fmt(3)) mu_2(fmt(3)) p(fmt(3))") ///
		collabels("Mean (treat=0)" "Mean (treat=1)" "p-value") ///
		label replace