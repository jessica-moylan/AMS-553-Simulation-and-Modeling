{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/jessica-moylan/AMS-553-Simulation-and-Modeling/blob/main/FraudProb.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 39,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "525mojwapipM",
        "outputId": "ad618733-163a-412a-b3d4-3aab843b7344"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-29.9154100427723\n",
            "-41.50622806804266\n",
            "-41.31061846467665\n",
            "-29.758906635260118\n",
            "-39.94874412106603\n",
            "-38.487425701712226\n",
            "-29.825576423105446\n",
            "-39.548351645631385\n",
            "-29.7028605196379\n",
            "-40.018969165990384\n"
          ]
        }
      ],
      "source": [
        "import math\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "\n",
        "# acceptance rejection threshold is k need to change\n",
        "k = 1\n",
        "#copied and pasted these for now but can call once uploaded to github\n",
        "FRAUD_MEAN = 140\n",
        "FRAUD_STANDARD_DEVIATION = 15\n",
        "FRAUD_PERCENT_BETWEEN_1_AND_4 = 0.2 # 0.113 from given data\n",
        "FRAUD_PERCENT_NOT_BETWEEN_1_AND_4 = 0.1 #0.0245 from given data\n",
        "\n",
        "\n",
        "dfPeople = pd.read_csv('people_data.csv')\n",
        "dfTT = pd.read_csv('transaction_table.csv')\n",
        "# x is going to be the row in the transaction table\n",
        "def NPtest (x):\n",
        "  person = dfTT.at[x, \"customer_id\"]\n",
        "  mu_p = dfPeople.at[person - 1, \"average_amount_per_transaction\"]\n",
        "  sd_p = dfPeople.at[person - 1, \"standard_deviation_amount_per_transaction\"]\n",
        "  transaction = dfTT.at[x, \"amount\"]\n",
        "  fraud_exp = -math.pow((math.log(transaction)-FRAUD_MEAN),2)/(2*(FRAUD_STANDARD_DEVIATION**2))\n",
        "  person_exp = -((math.log(transaction)-mu_p)**2)/(2*(sd_p**2))\n",
        "  fraud_Ln = math.log(1/(transaction*FRAUD_STANDARD_DEVIATION*math.sqrt(2*math.pi)))\n",
        "  person_Ln = fraud_Ln = math.log(1/(transaction*sd_p*math.sqrt(2*math.pi)))\n",
        "  LNK_result = fraud_Ln + fraud_exp - person_Ln - person_exp\n",
        "  return LNK_result\n",
        "for i in range(10):\n",
        "  if NPtest(i) < math.log(k):\n",
        "    print(NPtest(i))\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP8GIPJ4zpfQsmi5ky992jy",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}