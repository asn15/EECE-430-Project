from django.db import models

class Teams(models.Model):
  time = models.CharField(max_length=255)
  homeTeam = models.CharField(max_length=255)
  awayTeam = models.CharField(max_length=255)
  
  class Meta:
      verbose_name_plural = "Teams"


class BookingAndPurchasesHistory(models.Model):
  time = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  
  class Meta:
      verbose_name_plural = "Booking and Purchases History"

# SP: Starting Player / NS: Not Selected
class TeamFormationModel(models.Model):
  # STARTING PLAYERS
  GK_SP = models.CharField(max_length=255)        # Goalkeeper
  DF_SP_L = models.CharField(max_length=255)      # Defender
  DF_SP_LM = models.CharField(max_length=255)     # Defender
  DF_SP_RM = models.CharField(max_length=255)     # Defender
  DF_SP_R = models.CharField(max_length=255)      # Defender
  MF_SP_L = models.CharField(max_length=255)      # Midfielder
  MF_SP_LM = models.CharField(max_length=255)     # Midfielder
  MF_SP_RM = models.CharField(max_length=255)     # Midfielder
  MF_SP_R = models.CharField(max_length=255)      # Midfielder
  FW_SP_LW = models.CharField(max_length=255)     # Left Wing
  FW_SP_RW = models.CharField(max_length=255)     # Right Wing
  # PLAYERS ON BENCH / NOT SELECTED
  GK_NS = models.CharField(max_length=255)        # Goalkeeper
  DF_NS_1 = models.CharField(max_length=255)      # Defender
  DF_NS_2 = models.CharField(max_length=255)      # Defender
  MF_NS_1 = models.CharField(max_length=255)      # Midfielder
  MF_NS_2 = models.CharField(max_length=255)      # Midfielder
  FW_NS_LW = models.CharField(max_length=255)     # Left Wing
  FW_NS_RW = models.CharField(max_length=255)     # Right Wing

  class Meta:
      verbose_name_plural = "Team Formation"


class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Newsletter"