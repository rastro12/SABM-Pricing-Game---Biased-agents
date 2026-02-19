# SABM Pricing Game - Biased Agents Extension
This repository contains a modified version of the **Smart Agent-Based Modeling (SABM)** framework originally developed in:
> Han, Xu and Wu, Zengqing and Xiao, Chuan (2023).  
> *"Guinea Pig Trials" Utilizing GPT: A Novel Smart Agent-Based Modeling Approach for Studying Firm Competition and Collusion.*  
> arXiv:2308.10974

## About This Repository
This project builds upon the original SABM implementation and extends it to study **biased agent behavior** within economic simulations.
While the core architecture of the SABM framework is preserved, this version introduces modifications to agent decision-making processes in order to explore behavioral distortions and bias in strategic environments.
This repository represents an exploratory research extension of the original framework. No associated publication has been released yet.

## Modifications Introduced
Compared to the original SABM codebase, this repository includes:
- Implementation of biased agent behavior
- Adjustments to decision-making logic
- Modifications to simulation dynamics to analyze behavioral effects
- Changes to documentation reflecting this extended scope
The goal of these modifications is to investigate how bias influences agent interaction, competition outcomes, and emergent market dynamics.

## Setup
- Main Files
  - SABM_Economics_Main.py (Program Entry)
  - SABM_Economics_Data.py (Prompt)
  - SABM_Agent_Economics.py (Agent Class Definition)
    - GPT4_Core.py (Agent Class Definition)
- Function Component Files
  - Function_Plot.py (Result Visualization)
  - Function_Output.py (Output Path Designation)
  - Function_Theoretical_Solution.py (Economic Formulation)
- User Interface
  - GUI.py (User Interface)
- Tools
  - Figure_Plot_from_CSV.py (Result Visualization)

## Licence
This repository follows the original **MIT License** provided in the base implementation.

## Citation
If you use the original SABM framework, please cite:
```
@article{han2023guinea,
  title={"Guinea Pig Trials" Utilizing GPT: A Novel Smart Agent-Based Modeling Approach for Studying Firm Competition and Collusion},
  author={Han, Xu and Wu, Zengqing and Xiao, Chuan},
  journal={arXiv preprint arXiv:2308.10974},
  year={2023}
}
```
If you use this modified version, please also acknowledge that it extends the original SABM implementation.

## Disclarimer
This repository is an independent research extension and is not an official release by the original SABM authors.

